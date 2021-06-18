from time import sleep

from create_stock import create_stock
from interface.buyer_interface import BuyerInterfaceScreen
from interface.message_interface import MessageInterface
from interface.stock_interface import StockInterfaceScreen
from login.login import Login
from menu import Menu
from models.stock import Stock
from printable import display

_DELAY = 0.7
_STARTUP = False


def main():
    global _STARTUP
    running = True

    while running:

        if not _STARTUP:
            Menu.welcome_message()

            _STARTUP = True
        print("[+] Displaying login screen, please wait...")
        sleep(_DELAY)

        root_menu_choice = Menu.show_root_menu()

        if root_menu_choice == "1":

            login_id, password = Login.get_admin_login_credentials()

            if login_id.lower() == "admin" and Login.validate_login_details(login_id, password):
                print("\n[+] The password was successful, displaying administration screen")
                _get_admin_screen()
            else:
                print("\n[*] The password you entered is incorrect", end="\n")

        elif root_menu_choice == "2":
            login_id, password = Login.get_staff_login_credentials()

            if login_id == "staff01" and Login.validate_login_details(login_id, password):
                print("\n[+] The password was successful")
                go_to_purchase_screen(screen_title="Staff menu", display_staff_menu=True)
            else:
                print("[*] The password you entered is incorrect")

        elif root_menu_choice == "3":
            go_to_purchase_screen(screen_title="Student Menu", display_staff_menu=False)

        elif root_menu_choice == "4":
            print("[+[ Thanking you for using the virtual machine, see next time")
            sleep(0.5)
            print("[+] Goodbye")
            running = False

        else:
            print("[-] Incorrect choice entered, try entering number between 1-4")


def go_to_purchase_screen(screen_title, display_staff_menu):

    print(f"[+] Display {screen_title}, please wait..")
    sleep(_DELAY)
    display(Stock().stock(), screen_title, display_staff_stock=display_staff_menu)

    BuyerInterfaceScreen().go_to_purchase_item_screen()
    sleep(_DELAY)
    print("[+] Returning to main menu, please wait")
    sleep(_DELAY)


def _go_back_to_main_screen():
    print("[+] Going back root menu please wait...")
    sleep(_DELAY)
    main()


def _get_admin_screen():
    sleep(_DELAY)
    running = True

    while running:
        choice = Menu.admin_screen_display()

        if choice == "1":
            StockInterfaceScreen.go_to_add_item_stock_screen()
        elif choice == "2":
            StockInterfaceScreen.go_to_remove_item_from_stock_screen()
        elif choice == "3":
            StockInterfaceScreen().display_entire_stock_screen()
        elif choice == "4":
            StockInterfaceScreen().display_empty_stock_screen()
        elif choice == "5":
            stock_interface = StockInterfaceScreen()
            resp = stock_interface.get_update_item_screen()

            if resp == "m":
                print("\nPlease wait, returning to main menu")
                sleep(_DELAY)
                main()
        elif choice == "6":
            print("\n[+] Displaying message screen, please wait..")
            sleep(_DELAY)
            MessageInterface().go_to_message_screen()
            running = False
        elif choice == "7":
            _go_back_to_main_screen()

        else:
            print("[+] Incorrect choice try 1-7 ")


if __name__ == "__main__":
   create_stock()
   main()
