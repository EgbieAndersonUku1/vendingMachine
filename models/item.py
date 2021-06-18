
from time import sleep

from templates.item.item import ITEM_DISPLAY_TEMPLATE

_DELAY = 0.8

class Item(object):

    def __init__(self, item_id, name, price, quantity, for_staff, live):
        self.id = item_id
        self.name = name.title()
        self.price = price
        self.qty = int(quantity)
        self.for_staff = for_staff
        self.live = live

    @property
    def display(self):

        print("\n[*] Displaying item, please wait...")
        sleep(_DELAY)
        item = ITEM_DISPLAY_TEMPLATE.format(self.id, self.name, self.price, self.qty)
        print(item)
        print("[+] Item display complete", end="\n")
    
    def __repr__(self):
        return f"<Item: Name: {self.name}, Price: {self.price}, 'qty: {self.qty}>"

    def to_json(self):
        return self.__dict__.copy()



