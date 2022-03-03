'''Question 2:
Define a class named ``ItemInfo` with the following description:
item_code(Item Code), item(item name), price(Price of each item), qty(quantity in stock), 
discount(Discount percentage on the item), net_price(Price after discount)

Methods :
A member method calculate_discount() to calculate discount as per the following rules:

If qty <= 10 —> discount is 0
If qty (11 to 20 inclusive) —> discount is 15
If qty >= 20 —> discount is 20

A constructor init method to assign the initial values for item_code to 0 and price, qty, net_price and discount to null

A function called buy() to allow user to enter values for item_code, item, price, qty. 

Then call function calculate_discount() to calculate the discount and net_price(price * qty - discount).

A function show_all() or similar name to allow user to view the content of all the data members.

'''

class ItemInfo():

    # item_code(Item Code), item(item name), price(Price of each item), qty(quantity in stock), 
    # discount(Discount percentage on the item), net_price(Price after discount)

    def __init__(self, item_code = 0, item = 0, price = 0, qty = 0, discount = 0, net_price = 0):
        self.item_code = item_code
        self.item = item
        self.price = price
        self.qty = qty
        self.discount = discount
        self.net_price = net_price

    def buy(self):
        self.item_code = int(input("Please type the Item Code: "))
        self.item = input("Please type the Item Name: ")
        self.price = int(input("Please type the Item Price: "))
        self.qty = int(input("Please type the Item Quantity: "))
        self.discount = self.calculate_discount()
        self.net_price = int(self.price - self.price * self.discount/100)

    # to calculate the discount rate
    def calculate_discount(self):
        if self.qty <= 10:
            self.discount = 0
        elif 11 <= self.qty < 20:
            self.discount = 15
        elif self.qty >= 20:
            self.discount = 20

        return self.discount
                   
    # to allow user to view the content of all the data members
    def show_all(self):
        return(f'''
    Item Code   : {self.item_code}
    Item Name   : {self.item}
    Price       : {self.price}
    Discount (%): {self.discount}
    Net Price   : {self.net_price}
    ''')

# to create an object
order = ItemInfo()

# when we call the "buy()" method ask the datas from user
order.buy()

# to show the all datas to user
print(order.show_all())