from datetime import datetime
from uuid import uuid4

from database.db_storage import message_db


class MessageDB(object):

    msg_db = message_db

    def __init__(self, msg, subject=None, read=False, live=False, id=None, created_on=None):
        self.id = id
        self.msg = msg
        self.subject = subject
        self.read = read
        self.live = live
        self.created_on = datetime.now() if created_on is None else created_on

    @classmethod
    def delete_all_message(cls):
        for message in cls.get_all_messages():
            if message.live:
                message.live = False
                message.update()
        return True

    @classmethod
    def delete_msg_by_id(cls, msg_id):

        message = cls.get_msg_by_id(msg_id)
        if message:
            message.live = False
            message.update()
            return True
        return False

    @classmethod
    def get_all_messages(cls):
        return [cls.msg_db[msg_id] for msg_id in cls.msg_db if cls.msg_db[msg_id].live]

    @classmethod
    def get_all_read_messages(cls):
        return cls._filter_messages(read=True, live=True)

    @classmethod
    def get_all_unread_messages(cls):
        return cls._filter_messages(read=False, live=True)

    @classmethod
    def _filter_messages(cls, read, live):
        return [
            cls.msg_db[msg_id]
            for msg_id in cls.msg_db
            if cls.msg_db[msg_id].read == read and cls.msg_db[msg_id].live == live
        ]

    @classmethod
    def get_msg_by_id(cls, id):
        return cls.msg_db.get(id)

    @classmethod
    def mark_all_messages_as_read(cls):
        cls._mark_all_messages_helper(mark_message_as=True)

    @classmethod
    def mark_all_messages_as_unread(cls):
        cls._mark_all_messages_helper(mark_message_as=False)

    @classmethod
    def _mark_all_messages_helper(cls,  mark_message_as):
        for message in cls.get_all_messages():
            message.read = mark_message_as
            message.update()
        return True

    @classmethod
    def _mark_message_as_helper(cls, msg_id, mark_message_as):
        message = cls.get_msg_by_id(msg_id)
        if message:
            message.read = mark_message_as
            message.update()
            return True
        return False

    @classmethod
    def mark_message_as_read(cls, msg_id):
        return cls._mark_message_as_helper(msg_id, mark_message_as=True)

    @classmethod
    def mark_message_as_unread(cls, msg_id):
        return cls._mark_message_as_helper(msg_id, mark_message_as=False)

    def update(self):

        message = self.get_msg_by_id(self.id)
        if message:
            message.msg = self.msg
            message.read = self.read
            message.live = self.live
            message.subject = self.subject
            MessageDB.msg_db[self.id] = message
            return True
        return False

    def save(self):
        self.id = uuid4().hex[:4]
        self.live = True
        MessageDB.msg_db[self.id] = MessageDB(msg=self.msg, id=self.id,
                                              read=self.read, live=self.live,
                                              subject=self.subject, created_on=self.created_on)




