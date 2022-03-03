"""
Question 3:

Define a class named Product with the following specifications:

Data members:

product_id - A string to store product.
product_name - A string to store the name of the product.
product_purchase_price - A decimal to store the cost price of the product.
product_sale_price - A decimal to store 

Sale Price Margin - A decimal to be calculated as (product_sale_price - product_purchase_price)

Remarks - To store "Profit" if Margin is positive else "Loss" if Margin is negative.


Methods :

A constructor to intialize all the data members with valid default values.
A method set_remarks() that assigns Margin as (product_sale_price - product_purchase_price) and sets Remarks as mentioned below :
![h51](https://user-images.githubusercontent.com/98665012/155852165-694f473b-c1b2-4f35-8cac-74e1db4e6d86.png)

A method set_details() to accept values for product_id. product_name, product_purchase_price, product_sale_price and invokes SetRemarks() method.
A method get_details() that displays all the data members.

"""

class Product():

    # to intialize all the data members with valid default values
    def __init__ (self, product_id = "", product_name = "", product_purchase_price = 0, product_sale_price = 0, sale_price_margin = 0, remarks = ""):
        self.product_id = product_id
        self.product_name = product_name
        self.product_purchase_price = product_purchase_price
        self.product_sale_price = product_sale_price
        self.sale_price_margin = sale_price_margin
        self.remarks = remarks

    # to get data from user and calculate some data
    def set_details(self):
        self.product_id = input("\nPlease type the Product Id: ")
        self.product_name = input("Please type the Product Name: ")
        self.product_purchase_price = int(input("Please type the Product Purchase Price: "))
        self.product_sale_price = int(input("Please type the Product Sale Price: "))
        self.sale_price_margin = self.product_sale_price - self.product_purchase_price
        self.remarks = self.set_remarks()

    # to get the remarks (profit or loss)
    def set_remarks(self):
        if self.sale_price_margin < 0 :
            return "Loss"
        elif self.sale_price_margin > 0:
            return "Profit"
    
    # to allow user to view the content of all the data members
    def get_details(self):
        return(f'''
    Product Id          : {self.product_id}
    Product Name        : {self.product_name}
    Purchase Price      : {self.product_purchase_price}
    Sale Price          : {self.product_sale_price}
    Sale Price Margin   : {self.sale_price_margin}
    Remarks             : {self.remarks}
    ''')

# to create an object
order = Product()

# when we call the "set_details()" method ask the datas from user
order.set_details()

# to show the all datas to user
print(order.get_details())