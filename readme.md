
I recently applied for a freelance position contract. After getting past the initial first stage. The first of four stages I was offered a small 
programming task for the second stage in order to validate my problem solving skills and Python skills. The task is stated below.

### Problem requirements

A company has hired you to build a command line interface (CLI) for a virtual vending machine that must be programmed in Python.
The vending machine must be able to keep a record of the items in stock such as  'Item id', 'Price', 'Quantity', 
'Item name'. The vending machine must also give a receipt after every transaction has been made. It must display a 
different menu for employees and students. 

Do not use an external database or internal database such as SQLAlchemy, sqlite, MYSQL, etc to store data because we 
want to see how you use data structures.

The above requirement is a must and must be added to virtual vending machine but free feel to add any  extra features 
you want to the virtual vending machine, in fact we hope you do.


#### New Features added that are not part of the original requirements
    1. Administrator screen protected by a login and password
    
        1. The admin can add new items to the stock
        2. The admin can remove item from stock
        3. Display all items in stock
        4. Display empty stock
        5. Update the item in the stock e.g. quantity, price, etc
        6. Messages function 
            6.a sends message to admin:
                1. When an item has been sold
                2. When there are no more items in stock
                3. When an item has been added to the stock
                4. When an item has been removed from the stock
            
            6.b View messages
                1. View read messages
                2. View unread messages
                3. View all messages read and unread
                
            6.c Delete messages
                1. Delete a single message
                2. Delete all messages
                
    
    2. Staff screen protected by a login and password     
    3. Staff or Student can cancel the purchase and have the total amount they entered returned              
   
    
    

 ##### Virtual machine password
            1. Admin login credentials
                login ID -> admin
                password -> password
            
            2. Staff login credentials
                login ID -> staff01
                password -> 123456
                
     
    
 ### Virtual vending machine
 
            --------Login Screen-----------
    
    
               [1] Administrator
               [2] Staff
               [3] Student
               [4] Quit
               
               [+] Enter your choice: 1
               
               Enter the admin login ID: admin
               Enter the password: admin
               
               [+] The password was successful, displaying administration screen
               [+] Displaying admin menu...
               
                ------------Admin screen--------------
        
                [1] Add item to stock
                [2] Remove item from stock
                [3] Display all items in stock
                [4] Display empty items
                [5] Update stock
                [6] Messages
                [7] Main menu
                
                1. Add item to stock
                --------------------------------
                [+] Please enter your choice: 1
                [+] Enter the name for the item: pizza
                [+] Enter the price for the item: 2.25
                [+] Enter the qty for the item: 1
                [+] Is the item only for staff (y) for yes or any key for No: y
                [+] Would you like to add another item (y) for yes or any other key for no: n
                
                2. Remove item from stock
                ----------------------------------
                
                [+] Enter the ID of the item you want to remove: <id>
                [+] Successfully removed item from the item
                
                3. Update stock
                -------------------------------------
                [+] Please enter your choice: 5
                [+] Enter the ID of the stock you want to update or (M) for the (Main Menu): 
                
                [+] ID for item found, fetching update questions, please wait....

                [+] Do you want to change the item price (y) for YES or the (Enter key for NO): y
                [-] Enter the new item price (£): 2.25
                [+] Successfully updated item price
                [+] Do you want to change the qty (y) for YES or (Enter key for NO): y
                [+] Successfully updated price quantity
                [+] Do you want to view the updated item (y) for YES or the (Enter key for NO): y
                [*] Displaying item, please wait...


                <--------------- ITEM ------------------------>
                
                
                        ID       : 3bf2
                        Name     : Foster
                        Price    : 2.25
                        Quantity : 1
                        
                <--------------- END ITEM DISPLAY ------------->
                
                [+] Item display complete
                [+] Done
                
                
                3. Messages
                
                ------------Admin screen--------------
        
                [1] Add item to stock
                [2] Remove item from stock
                [3] Display all items in stock
                [4] Display empty items
                [5] Update stock
                [6] Messages
                [7] Main menu
                -------------------------------------
                
                [+] Enter your choice: 6
                
                ----------- Message Screen ------------

                [1] View messages
                [2] Delete messages
                [3] Back to main screen
                
                [+] Enter your choice:  1
                
                ----------- View messages ------------

                [1] View read messages
                [2] View unread messages
                [3] View all messages read and unread
                [4] Back to main screen

                ----------------------------------------------------
                
                
                ----------- Message Screen ------------

                [1] View messages
                [2] Delete messages
                [3] Back to main screen
                
                [+] Enter your choice:  2
                
                 ----------- Delete messages ------------

                [1] Delete a single message
                [2] Delete all messages
                [3] Back to main screen
                 
                


### Usage
To run it simple type python app.py after you have downloaded or clone the project.