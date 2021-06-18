from time import sleep

_DELAY = 0.8


def display(stock, title, display_staff_stock=False, admin=False):

    if not stock:
        print("\n[+] There is no stock to display.")

    else:
        if admin:
            print("[+] Fetching admin screen..")
            sleep(_DELAY)
            print("[+] Displaying both empty and non-empty stock")
            sleep(_DELAY)
            print("[+] Fetching items from stock database, please wait..")
            sleep(_DELAY)
            print("[+] Done")
            print(f"\n----------------------- ADMIN SCREEN --------------------------------------\n")

        else:
            print(f"\n----------------------- {title} --------------------------------------\n")

        for item in stock:

            if admin:
                item_qty = "EMPTY STOCK" if not item.qty else item.qty
                print(f"[*] Item ID: {item.id}, {item.name} -> £{item.price}, Qty -> {item_qty} ")
            elif display_staff_stock and item.for_staff and item.qty > 0:
                print(f"[*] Item ID: {item.id}, {item.name} (£{item.price}), Qty -> {item.qty} ")
            elif not item.for_staff and item.qty > 0:
                print(f"[*] Item ID: {item.id}, {item.name} (£{item.price}) , Qty -> {item.qty} ")

        print("\n------------------------ END ------------------------------------------")








