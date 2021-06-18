from time import sleep

from models.stock import Stock
from printable import display
from security.security import get_valid_input, get_valid_number

_DELAY = 0.5


class StockInterfaceScreen(object):

    def __init__(self):
        self._stock = Stock()
        self._item_id = None

    def display_all_items_in_stock_screen(self):
        print("[*] Displaying all available items in stock")
        sleep(_DELAY)
        display(self._stock.get_items_in_stock(), title="Displaying available item")

    def display_empty_stock_screen(self):
        print("[*] Displaying all unavailable stock, please wait...")
        sleep(_DELAY)
        display(self._stock.get_items_not_in_stock(), title="Displaying unavailable item in stock", admin=True)

    def display_entire_stock_screen(self):
        print("[+] Displaying entire stock, please wait..")
        sleep(_DELAY)
        display(self._stock.stock(), title="Entire items in stock", admin=True)

    @staticmethod
    def go_to_remove_item_from_stock_screen():

        stock_id = get_valid_input("[+] Enter the ID of the item you want to remove: ")
        if Stock.remove_by_id(stock_id):
            print("[+] Successfully removed item from the item")
        else:
            print("[-] Failed to remove product from the item because the ID entered was incorrect")

    @classmethod
    def go_to_add_item_stock_screen(cls):

        while True:
            title, price, quantity, staff = cls.prompt_user_for_item_details()
            Stock.add(title, price, quantity, staff)

            choice = input("\n[+] Would you like to add another item (y) for yes or any other key for no: ")
            if choice == "y":
                continue
            break

    @classmethod
    def prompt_user_for_item_details(cls):

        title = get_valid_input("[+] Enter the name for the item: ")
        price = get_valid_number("[+] Enter the price for the item: ")
        quantity = get_valid_input("[+] Enter the qty for the item: ")

        resp = get_valid_input("[+] Is the item only for staff (y) for yes or enter for No: ")
        if resp.lower() == "y":
            print("[+] The item will only be added to the staff menu", end="\n")
            sleep(1)
            staff = True
        else:
            print("[+] The item will be added to both the staff and student menu")
            staff = False
        return title, price, quantity, staff

    def get_update_item_screen(self):

        while True:
            item_id = input("[+] Enter the ID of the stock you want to update or (M) for the (Main Menu): ")

            if item_id and item_id.lower() == "m":
                return item_id.lower()
            elif item_id and Stock.search_by_id(item_id):
                self._item_id = item_id
                print("[+] ID for item found, fetching update questions, please wait....")
                sleep(1)
                self._get_questions_for_update()
                print("[+] Done")
            else:
                print("[-] There is not item in stock with that id")

    def _get_questions_for_update(self):

        item = None

        price = input("\n[+] Do you want to change the item price (y) for YES or the (Enter key for NO): ")

        if price.lower() == "y":
            item = self._update_item_helper(self._item_id, update_price=True)
            print("[+] Successfully updated item price", end="\n")

        quantity = input("[+] Do you want to change the qty (y) for YES or (Enter key for NO): ")

        if quantity == "y":
            item = self._update_item_helper(self._item_id, update_qty=True)
            print("[+] Successfully updated price quantity", end="\n")
        if item:

            sleep(_DELAY)
            self.view_updated_item_screen(item)
            return True

    def _update_item_helper(self, item_id, update_price=False, update_qty=False):

        running = True
        item = None

        while running:

            if update_price:
                price = get_valid_number("[-] Enter the new item price (£): ")
                if price:
                    item = Stock.update_price(item_id, price)
                    running = False
            elif update_qty:
                qty = int(get_valid_number("[-] Enter the new qty: "))
                if qty:
                    item = Stock.update_quantity(item_id, qty)
                    running = False
        return item

    def view_updated_item_screen(self, item):

        choice = input("[+] Do you want to view the updated item (y) for YES or the (Enter key for NO): ")
        item.display if choice == "y" else None



