from database.stock_db import StockDB
from models.message import Message
from templates.message.message import ADD_STOCK_MESSAGE_STRING_TEMPLATE, EMPTY_STOCK_STRING_TEMPLATE, \
     REMOVE_STOCK_STRING_MESSAGE_TEMPLATE, UPDATED_PRICE_STRING_TEMPLATE, UPDATED_STOCK_STRING_TEMPLATE


class Stock(object):

    @classmethod
    def add(cls, name: str, price: float, quantity: int, staff=False) -> bool:

        StockDB(name=name, price=price, qty=quantity, staff=staff).save()

        msg = ADD_STOCK_MESSAGE_STRING_TEMPLATE.format(name.title(), price, quantity)
        Message(subject="Re: New item added", msg=msg).send()

    def get_items_in_stock(self):
        return self._get_items_helper()

    def get_items_not_in_stock(self):
        return self._get_items_helper(get_items_in_stock=False)

    def _get_items_helper(self, get_items_in_stock=True):

        stock = []

        items = StockDB.get_all_stock()

        for item in items:
            if not item.live:
                continue
            elif get_items_in_stock:
                if item.qty > 0:
                    stock.append(item)
            elif not get_items_in_stock:
                if not item.qty:
                    stock.append(item)

        return stock

    @classmethod
    def update_price(cls, item_id, new_price):

        item = StockDB.update_price(item_id, float(new_price))

        if item:
            msg = UPDATED_PRICE_STRING_TEMPLATE.format(item.id, item.name, item.price)
            Message(subject="Re: Item price update", msg=msg).send()
            return item
        return False

    @classmethod
    def update_quantity(cls, id, new_quantity):

        item = StockDB.get_stock_by_id(id)

        if item:
            item = StockDB.update_quantity(item_id=item.id, quantity=new_quantity)

            if item and not item.qty:
                msg = EMPTY_STOCK_STRING_TEMPLATE.format(item.id, item.name)
                subject = "Re: Empty stock"
            else:
                msg = UPDATED_STOCK_STRING_TEMPLATE.format(item.id, item.qty)
                subject = "Re: Item quantity update"

            Message(subject=subject, msg=msg).send()

            return item
        return False

    @staticmethod
    def remove_by_id(item_id):

        if StockDB.remove_item_by_id(item_id):
            msg = REMOVE_STOCK_STRING_MESSAGE_TEMPLATE.format(item_id)
            Message(subject="Re: An item has been removed", msg=msg).send()

            return True
        return False

    @staticmethod
    def search_by_id(id):
        return StockDB.get_stock_by_id(id)

    def stock(self):
        return StockDB.get_all_stock()



