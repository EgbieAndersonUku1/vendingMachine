from time import sleep

from menu import Menu
from models.message import Message
from security.security import get_valid_input
from templates.message.message import CHOICE_MSG_STRING_TEMPLATE, SEND_MESSAGE_TEMPLATE


class MessageInterface(object):

    def __init__(self):
        self._msg = Message()

    def go_to_message_screen(self):
        running = True

        while running:
            choice = Menu.display_message_screen()

            if choice == "1":
                print("[+] Displaying view message screen, please wait", end="\n")
                sleep(1)
                self._go_to_view_messages()
            elif choice == "2":
                print("[+] Displaying delete message screen, please wait", end="\n")
                sleep(1)
                self._go_to_delete_messages()
            elif choice == "3":
                print("[+] Returning to menu, please wait")
                running = False
            else:
                print("[+] Incorrect choice, choice must be between 1-3")
        return

    def _go_to_view_messages(self):

        running = True

        choice = Menu.view_messages()

        while running:
            if choice == "1":
                self._display_messages_helper(messages=self._msg.get_all_read_msg(), title="READ MESSAGES")
                sleep(1)
                self._prompt_user_if_they_want_mark_message_as_unread()
            elif choice == "2":
                self._display_messages_helper(messages=self._msg.get_all_unread_msg(), title="UNREAD MESSAGES")
                sleep(1)
                self._prompt_user_if_they_want_mark_message_as_read()
            elif choice == "3":
                self._display_messages_helper(messages=Message.get_all_messages(), title="MESSAGES", all_messages=True)
                self._prompt_user_if_they_want_view_message()
                print("[+] Returning to message menu, please wait")
            elif choice == "4":
                running = False
            else:
                print("[+] Incorrect choice, choice must be between 1-4")

    def _go_to_delete_messages(self):

        running = True

        while running:
            choice = Menu.delete_messages()
            if choice == "1":
                self._prompt_user_for_message_id_to_delete()
            elif choice == "2":
                print("[+] Deleting all messages, please wait...")
                Message.delete_all_messages()
                sleep(1)
                print("[+] Done")
            elif choice == "3":
                running = False
            else:
                print("[+] Incorrect choice, choice must be between 1-3")

    def _display_messages_helper(self, messages, title, all_messages=False):

        if not messages:
            print(f"[+] There are no {title.title()} to show")
            self.go_to_message_screen()

        else:
            print("\n\nFetching messages please wait...\n\n")
            sleep(0.5)
            print(f"<-------------------------------- {title} ----------------------------------------------->\n")

            for index, message in enumerate(messages):
                if all_messages:
                    message_read_status = "Message status: read" if message.read == True else "Message status: unread"
                    print(f"[+] Msg ID: {message.id},  message: {message.msg[:65]}... <{message_read_status}>")
                else:
                    print(f"[+] Msg ID: {message.id},  message: {message.msg[:30]}...")

            print("\n<-------------------------------- END OF MESSAGES -------------------------------------->", end="\n")

    def _prompt_user_for_message_id_to_delete(self):

        running = True

        while running:
            msg_id = get_valid_input("\n[+] Enter the message id you want to delete or (b) to go back: ")

            if msg_id.lower() == "b":
                running = False
                print("[+] Returning to message menu, please wait...")
                sleep(1)
            elif Message.delete_msg(msg_id):
                print("[+] Successfully, deleted message")
            else:
                print("[-] Failed to delete message because the msg ID received is incorrect")

    def _prompt_user_if_they_want_mark_message_as_read(self):

        msg = CHOICE_MSG_STRING_TEMPLATE.format("R", "read", "V")
        resp = get_valid_input(msg)

        if resp.lower() == "r":
            sleep(0.5)
            print(self._mark_message_helper(mark_message_as="read", mark_message_as_func=Message.mark_message_as_read))
        else:
            self._execute_choice(resp, "read", Message.mark_all_messages_as_read)

    def _prompt_user_if_they_want_mark_message_as_unread(self):

        msg = CHOICE_MSG_STRING_TEMPLATE.format("U", "unread", "V")
        resp = get_valid_input(msg)
        if resp.lower() == "u":
            sleep(0.5)
            print(self._mark_message_helper(mark_message_as="unread", mark_message_as_func=Message.mark_message_as_unread))
        else:
            self._execute_choice(resp, "unread", Message.mark_all_messages_as_unread)

    def _execute_choice(self, choice, mark_message_as, mark_all_message_as_func):

        if choice.lower() == "b":
            self.go_to_message_screen()
        elif choice.lower() == "a":
            print(f"[+] Marking all messages as {mark_message_as}, please wait... ")
            mark_all_message_as_func()
            sleep(0.5)
            print(f"[+] Successfully marked all messages as {mark_message_as}")
        elif choice.lower() == "v":
            self._prompt_user_if_they_want_view_message()

    def _mark_message_helper(self, mark_message_as, mark_message_as_func):

        msg_id = get_valid_input(f"[+] Enter the msg ID you want to mark as {mark_message_as}: ")
        resp = f"[+] Successfully mark message as {mark_message_as}" if mark_message_as_func(msg_id) \
                else f"[-] Failed to mark message as {mark_message_as}"
        return resp

    def _prompt_user_if_they_want_view_message(self):
        resp = input("\n[+] Do you want to view a message (y) YES or Enter key to return to main message menu: ")

        if resp.lower() == "y":
            running = True
            while running:
                msg_id = input("[+] Enter the message id: ")
                msg = Message.get_msg_by_id(msg_id)
                if msg:
                    self._view_message(msg)
                    running = False
                else:
                    print("[-] Incorrect message id entered, please try again")
        else:
            print("[+] Returning to the main message menu, please wait..\n")
            self.go_to_message_screen()
            sleep(1)

    def _view_message(self, msg):

        print("[+] Checking if message is read or unread, please wait")
        sleep(1)
        if msg.read:
            print("[+] Message has already been marked as read, no need to mark message as read")
        else:
            print("[+] Marking message as read, please wait...")
            Message.mark_message_as_read(msg.id)
            sleep(1)
            print("[+] Successfully marked message")
        sleep(1)
        print("[+] Display message please wait..")
        sleep(1)
        msg_template = SEND_MESSAGE_TEMPLATE.format(msg.subject, msg.msg, msg.created_on)
        print(msg_template)
        get_valid_input("[+] Press any key plus enter the key to continue: ")
        print("[+] Display complete")
        sleep(1)

