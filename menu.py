from security.security import get_valid_input
from templates.menu.menu import WELCOME_MENU


class Menu(object):

    @staticmethod
    def admin_screen_display():
        print(""" 

                ------------Admin screen--------------
        
                [1] Add item to stock
                [2] Remove item from stock
                [3] Display all items in stock
                [4] Display empty items
                [5] Update stock
                [6] Messages
                [7] Main menu
      
        """)
        return get_valid_input("[+] Please enter your choice: ")

    @staticmethod
    def display_message_screen():
        print("""
                ----------- Message Screen ------------

                [1] View messages
                [2] Delete messages
                [3] Back to main screen

            """)
        return get_valid_input("[+] Enter your choice: ")

    @staticmethod
    def welcome_message():
        print(WELCOME_MENU)
        return input("[+] Press the Enter key to continue: ")

    @staticmethod
    def view_messages():
        print("""
                ----------- View messages ------------

                [1] View read messages
                [2] View unread messages
                [3] View all messages read and unread
                [4] Back to main message menu

             """)
        return get_valid_input("[+] Enter your choice: ")

    @staticmethod
    def delete_messages():
        print("""
                ----------- Delete messages ------------

                [1] Delete a single message
                [2] Delete all messages
                [3] Back to message menu

                 """)
        return get_valid_input("[+] Enter your choice: ")

    @staticmethod
    def show_root_menu():
        print(""" 

               --------Login Screen-----------
    
    
               [1] Administrator
               [2] Staff
               [3] Student
               [4] Quit


           """)

        return get_valid_input("[+] Enter your choice: ")


