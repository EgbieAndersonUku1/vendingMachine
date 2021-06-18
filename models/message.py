from database.message_db import MessageDB


class Message(object):

    def __init__(self, msg=None, subject=None):
        self._msg = msg
        self._subject = subject

    def send(self):

        if self._msg:
            MessageDB(msg=self._msg, subject=self._subject).save()
            self._msg = None
            return True
        return False

    @staticmethod
    def mark_all_messages_as_read():
        return MessageDB.mark_all_messages_as_read()

    @staticmethod
    def delete_all_messages():
        return MessageDB.delete_all_message()

    @staticmethod
    def mark_all_messages_as_unread():
        return MessageDB.mark_all_messages_as_unread()

    @classmethod
    def delete_msg(cls, msg_id):
        return MessageDB.delete_msg_by_id(msg_id)

    @classmethod
    def mark_message_as_unread(cls, msg_id):
        return MessageDB.mark_message_as_unread(msg_id)

    @classmethod
    def mark_message_as_read(cls, msg_id):
        return MessageDB.mark_message_as_read(msg_id)

    @classmethod
    def get_msg_by_id(cls, msg_id):
        return MessageDB.msg_db.get(msg_id)

    @staticmethod
    def get_all_messages():
        return MessageDB.get_all_messages()

    def get_all_read_msg(self):
        return MessageDB.get_all_read_messages()

    def get_all_unread_msg(self):
        return MessageDB.get_all_unread_messages()

    def __repr__(self):
        return f"<{self._msg[:6]}....>"


