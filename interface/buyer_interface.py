from time import sleep

from models.message import Message
from models.receipt import Receipt
from models.stock import Stock
from security.security import get_valid_input
from templates.message.message import ITEM_BOUGHT_STRING_TEMPLATE
from utils.calculator import Calculate


class BuyerInterfaceScreen(object):

    def __init__(self):
        self._item = None
        self._receipt = None
        self._amount_received = 0
        self._is_purchase_cancelled = False

    def go_to_purchase_item_screen(self):

        running = True

        self._prompt_user_for_item_id()

        while running:

            if not self._is_purchase_cancelled:
                self._item.display
            if self._purchase_item():
                running = False
            elif self._is_purchase_cancelled:
                running = False

        return True

    def _purchase_item(self):

        is_amount_remaining = False

        while self._amount_received < self._item.price:

            if self._is_purchase_cancelled:
                return False
            elif not is_amount_remaining:

                self._amount_received += self._prompt_user_for_item_amount()
                remaining_balance = self._get_remaining_balance()

                if remaining_balance > 0:
                    print("[+] Remaining amount £{}".format(round(remaining_balance, 2)))
                    is_amount_remaining = True

            elif is_amount_remaining:

                self._amount_received += self._prompt_user_for_the_remaining_item_amount()
                remaining_balance = self._get_remaining_balance()

                if remaining_balance <= 0:
                    is_amount_remaining = False
                else:
                    print("[+] Remaining amount £{}".format(round(remaining_balance, 2)))

            self._prompt_user_if_they_want_cancel_purchase()

        if not self._is_purchase_cancelled:
            Stock.update_quantity(id=self._item.id, new_quantity=int(self._item.qty) - 1)
            Receipt(self._item, self._get_change(), self._amount_received).print_receipt()
            msg = ITEM_BOUGHT_STRING_TEMPLATE.format(self._item.id, self._item.name.title(), self._item.price)
            Message(subject="An item has been sold", msg=msg).send()
            self._item = None

        return True

    def _get_change(self):

        change = None

        if self._amount_received > self._item.price:
            change = Calculate(self._amount_received, self._item.price).calculate()
        elif self._amount_received == self._item.price:
            change = 0.00
        return change

    def _prompt_user_for_the_remaining_item_amount(self):
        return self._prompt_user("[+] Enter the remaining amount (£) : ")

    def _get_remaining_balance(self):
        return Calculate(self._item.price, self._amount_received).calculate()

    def _prompt_user_for_item_amount(self):
        return self._prompt_user("\n[+] Enter the amount for the item: ")

    def _prompt_user(self, prompt):
        running = True

        while running:
            try:
                amount = float(input(prompt))
            except ValueError:
                print("[-] The amount entered must be a float or an integer, try again...")
                continue

            if amount < 0:
                print("[-] The amount entered cannot be a negative value, please try adding a positive value")
            else:
                running = False

        return amount

    def _prompt_user_for_item_details(self):

        title = get_valid_input("Enter the name of the product to add to the item: ")
        price = get_valid_input("Enter the item price of the item: ")
        quantity = get_valid_input("Enter the qty for the item: ")
        staff = get_valid_input("Add this item only to the staff menu (y: yes or any key for no): ")

        return title, price, quantity, staff

    def _prompt_user_if_they_want_cancel_purchase(self):

        choice = input("\n[*] Enter (c) to cancel the order or enter any key to continue with the present order:  ")

        if choice == "c":
            self._is_purchase_cancelled = True
            amount_entered = round(self._amount_received, 2)
            print("[+] Cancelling order, returning the total amount user entered, please wait..")
            sleep(1)
            print(f"[+] Successfully returned the total amount of £{amount_entered} entered by user")
            sleep(0.5)
            return True
        return False

    def _prompt_user_for_item_id(self):

        running = True

        while running:
            product_id = input("\n[+] Enter the product ID for the item you want to purchase: ")
            item = Stock.search_by_id(product_id)
            if not item:
                print("[-] The item details could not be retrieved because the ID entered is incorrect..")
            else:
                running = False
        self._item = item


