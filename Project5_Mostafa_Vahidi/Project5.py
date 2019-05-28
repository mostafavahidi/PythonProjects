'''Mostafa Vahidi
CS 2990.01 Python Prof. Yang
Project 5
'''

import sys


class ItemToPurchase(object):
    item_name = "none"
    item_price = 0.0
    item_quantity = 0
    item_description = "none"

    
    def __init__(self,item_name, item_price, item_quantity, item_description):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        return "{} {} @ ${} = ${}".format(self.item_name, self. item_quantity, self. item_price, self.item_quantity * self.item_price)
    

class ShoppingCart(object):
    listOfItems = []
    cust_name = "none"
    cust_date = "January 1, 2016"
    
    def __init__(self, cust_name, cust_date):
        self.cust_name = cust_name
        self.cust_date = cust_date

    def add_item(self, itemToPurchase):
        self.listOfItems.append(itemToPurchase)

    def remove_item(self, itemName):
        found = False
        for i in self.listOfItems:
            if i.item_name == itemName :
                self.listOfItems.remove(i)
                found = True
        if found == False:
            print("Item was not found. Nothing removed")

    def modify_item(self, ItemToPurchase):
        found = False
        for i in self.listOfItems:
            if i.item_name == ItemToPurchase.item_name:
                i.item_price = ItemToPurchase.item_price
                i.item_quantity = ItemToPurchase.item_quantity
                i.item_description = ItemToPurchase.item_description
                found = True            

        if found == False:
            print("Item not found in cart. Nothing modified")


    def get_num_items_in_cart(self):
        numItems = 0
        for i in self.listOfItems:
            numItems += i.item_quantity
        return numItems
    
    def get_cost_of_cart(self):
        price = 0
        for i in self.listOfItems:
            price += i.item_quantity * i.item_price
        return price
    
    def print_total(self):
        if len(self.listOfItems) == 0:
            print("shopping cart is empty")
        else:
            return self.get_cost_of_cart()

    def print_price_breakdown(self):
        for i in self.listOfItems:
            print(i.print_item_cost())

    def print_descriptions(self):
        for i in self.listOfItems:
            print(str(i.item_name) + ": " + str(i.item_description))


def print_menu(ShoppingCart):
    print("a - Add item to cart \n r - Remove item from cart \n c - Change item quantity \n i - Output items' descriptions \n o - Output shopping cart \n q - quit")
    userChoice = input(print("Type your choice here: "))
    if userChoice == 'a':
        print("ADD ITEM TO CART")
        itemNameToAdd = input(print("Enter the item name: "))
        itemDescriptionToAdd = input(print("Enter the item description: "))
        itemPriceToAdd = float(input(print("Enter the item price: ")))
        itemQuantityToAdd = int(input(print("Enter the item quantity: ")))

        itemToAdd = ItemToPurchase(itemNameToAdd, itemPriceToAdd, itemQuantityToAdd, itemDescriptionToAdd)
        ShoppingCart.add_item(itemToAdd)
                        
    elif userChoice == 'r':
        print("REMOVE ITEM FROM CART")
        nameOfItemToRemove = input(print("Enter the item name: "))
        ShoppingCart.remove_item(nameOfItemToRemove)
        
    elif userChoice == 'c':
        print("CHANGE ITEM QUANTITY")
        nameOfItem = input(print("Enter the item name: "))
        newQuantity = int(input(print("Enter the new quantity: ")))

        itemToMod = ItemToPurchase(nameOfItem, 0.0, newQuantity, "none")
        ShoppingCart.modify_item(itemToMod)
        
        
    elif userChoice == 'i':
        print("OUTPUT ITEMS' DESCRIPTIONS")
        print(ShoppingCart.cust_name + "'s Shopping Cart - " + ShoppingCart.cust_date)
        print("\n Item Descriptions")
        print(ShoppingCart.print_descriptions())
            
    elif userChoice == 'o':
        print("OUTPUT SHOPPING CART")
        print(ShoppingCart.cust_name + "'s Shopping Cart - " + ShoppingCart.cust_date)
        print("Number of items: " + str(ShoppingCart.get_num_items_in_cart()))
        print(ShoppingCart.print_price_breakdown())
        print("Total: " + str(ShoppingCart.print_total()))

    elif userChoice == 'q':
        print("Have a nice day! Bye")
        sys.exit(0)

    else:
        print("Not a valid input, let's try this again.")
        print_menu(ShoppingCart)

    print_menu(ShoppingCart)
    

def main():
    cust_name = input(print("Enter customer's name:"))
    cust_date = input(print("Enter customer's date:"))

    newShoppingCart = ShoppingCart(cust_name, cust_date)
    #newShoppingCart.cust_date = cust_date
    #newShoppingCart.cust_name = cust_name
    
    print_menu(newShoppingCart)


    
main()


'''
ADDING ITEMS******************************************************

Enter customer's name:
NoneMostafa
Enter customer's date:
NoneNov 19, 2018
a - Add item to cart 
 r - Remove item from cart 
 c - Change item quantity 
 i - Output items' descriptions 
 o - Output shopping cart 
 q - quit
Type your choice here: 
Nonea
ADD ITEM TO CART
Enter the item name: 
NoneNike Romaleos
Enter the item description: 
NoneVolt color, weightlifting shoes
Enter the item price: 
None189
Enter the item quantity: 
None2
a - Add item to cart 
 r - Remove item from cart 
 c - Change item quantity 
 i - Output items' descriptions 
 o - Output shopping cart 
 q - quit
Type your choice here: 
Nonea
ADD ITEM TO CART
Enter the item name: 
NoneTomatoes
Enter the item description: 
NoneVegetable, red colored
Enter the item price: 
None5
Enter the item quantity: 
None2
a - Add item to cart 
 r - Remove item from cart 
 c - Change item quantity 
 i - Output items' descriptions 
 o - Output shopping cart 
 q - quit
Type your choice here: 
Noneo
OUTPUT SHOPPING CART
Mostafa's Shopping Cart - Nov 19, 2018
Number of items: 4
Nike Romaleos 2 @ $189.0 = $378.0
Tomatoes 2 @ $5.0 = $10.0
None
Total: 388.0


REMOVING ITEMS**************************************************
a - Add item to cart 
 r - Remove item from cart 
 c - Change item quantity 
 i - Output items' descriptions 
 o - Output shopping cart 
 q - quit
Type your choice here: 
Noner
REMOVE ITEM FROM CART
Enter the item name: 
NoneChocolate Chips
Item was not found. Nothing removed

REMOVE ITEM FROM CART
Enter the item name: 
NoneTomatoes
a - Add item to cart 
 r - Remove item from cart 
 c - Change item quantity 
 i - Output items' descriptions 
 o - Output shopping cart 
 q - quit
Type your choice here: 
Noneo
OUTPUT SHOPPING CART
Mostafa's Shopping Cart - Nov 19, 2018
Number of items: 0
None
shopping cart is empty



CHANGING ITEM QUANTITY*****************************************
CHANGE ITEM QUANTITY
Enter the item name: 
NoneNike Romaleos
Enter the new quantity: 
None3
a - Add item to cart 
 r - Remove item from cart 
 c - Change item quantity 
 i - Output items' descriptions 
 o - Output shopping cart 
 q - quit
Type your choice here: 
Noneo


Enter customer's name:
NoneMostafa
Enter customer's date:
NoneNov 17 2017
a - Add item to cart 
 r - Remove item from cart 
 c - Change item quantity 
 i - Output items' descriptions 
 o - Output shopping cart 
 q - quit
Type your choice here: 
Noner
REMOVE ITEM FROM CART
Enter the item name: 
Nonecookies
Item was not found. Nothing removed




OUTPUT ITEMS' DESCRIPTIONS**************************************
a - Add item to cart 
 r - Remove item from cart 
 c - Change item quantity 
 i - Output items' descriptions 
 o - Output shopping cart 
 q - quit
Type your choice here: 
Nonei
OUTPUT ITEMS' DESCRIPTIONS
Mostafa's Shopping Cart - Nov 19, 2018

 Item Descriptions
Nike Romaleos: Weightlifting shoes
Tomatoes: Red colored






OUTPUT SHOPPING CART**********************************************

a - Add item to cart 
 r - Remove item from cart 
 c - Change item quantity 
 i - Output items' descriptions 
 o - Output shopping cart 
 q - quit
Type your choice here: 
Noneo
OUTPUT SHOPPING CART
Mostafa's Shopping Cart - Nov 19, 2018
Number of items: 4
Nike Romaleos 2 @ $189.0 = $378.0
Tomatoes 2 @ $4.0 = $8.0
None
Total: 386.0

'''







        
