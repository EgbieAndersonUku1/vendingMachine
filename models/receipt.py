

from datetime import datetime
from time import sleep

from templates.receipt.receipt import RECEIPT_TEMPLATE


class Receipt(object):

    def __init__(self, item, change, amount_received):
        self._item = item
        self._change = round(change, 2)
        self._amount_received = round(amount_received, 2)

    def print_receipt(self):
        purchase_date = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        sleep(0.1)

        print("[+] Displaying receipt, please wait...")
        sleep(0.5)

        receipt = RECEIPT_TEMPLATE.format(self._item.id, self._item.name, self._item.price,
                                          purchase_date, self._amount_received, self._change)
        print(receipt)
        input("Press enter to continue: ")
        return True

    def _to_json(self):
        return self.__dict__.copy()

