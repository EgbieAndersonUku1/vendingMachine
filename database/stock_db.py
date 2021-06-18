from uuid import uuid4

from database.db_storage import store_db
from models.item import Item


class StockDB(object):

    def __init__(self, name, price, qty, staff, id=None):
        self.id = id
        self.name = name
        self.price = price
        self.qty = qty
        self.staff = staff

    @staticmethod
    def get_all_stock():
        return [store_db[_id]['item'] for _id in store_db if store_db[_id]['item'].live]

    @staticmethod
    def get_stock_by_id(id):
        item = store_db.get(id)
        if item:
            return item['item']
        
    @classmethod
    def remove_item_by_id(cls, item_id):
        item = cls._update_helper(item_id, remove_item=True)
        return True if item and not item.live else False

    @classmethod
    def update_price(cls, item_id, new_price):
        return cls._update_helper(item_id, price=new_price, update_price=True)

    @classmethod
    def update_quantity(cls, item_id, quantity):
        return cls._update_helper(item_id, quantity=quantity, update_qty=True)

    @classmethod
    def _update_helper(cls, item_id, price=None, quantity=None, update_price=False, update_qty=False, remove_item=False):

        item = cls.get_stock_by_id(item_id)

        if item:
            if update_price:
                item.price = price
            elif update_qty:
                item.qty = int(quantity)
            elif remove_item:
                item.live = False
            store_db[item_id] = {"item": item}
            return item

    def save(self):
        self.id = uuid4().hex[:4]
        self.live = True
        item = Item(item_id=self.id, name=self.name, price=self.price,
                    quantity=self.qty, for_staff=self.staff, live=self.live)

        store_db[self.id] = {"item": item}
        return item

    def to_json(self):
        return self.__dict__.copy()
