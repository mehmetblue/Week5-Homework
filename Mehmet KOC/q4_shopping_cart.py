"""

Question 4:
Write a Customer class and Items class. Let user enter customer information and add stuff to his/her shopping card.

Class Items : Method : __init__(), __str__(), calculate_discount(), shopping_cart(), get_total_amount()

calculate_discount():

total_price = price * qty
discount —> 25% if total_price >= 4000
discount —> 15% if total_price >= 2000
discount —> 10% if total_price < 2000
price_tobe_paid = total_price – discount
shopping_cart():

Let user add items in the shopping basket. Be creative with the items, set their prices as well.

__str__():

Print items added and total price nicely. Class Customer : Methods: __init__()``, get_cust_info()this is optional,str()`
Optionally create a get_cust_info() or similar to allow customer to enter his/her information or just define them in __init__() and pass customer information as arguments while creating a customer object.

__str__():

Print customer information and price nicely. Find a way to link two classes. For example, instances of both classes may have a customer number. With a get method, get the customer number and pass it to the item object as an argument to set customer number attribute. So Customer class instance holds the customer info, Items class holds the shopped item’s info for the same customer ID number such as price, quantity or so.

In the end, print both info (customer info and shopped items info) using their respective __str__ format in a nice way.
Simple example:

Customer1 = [name : Jack, last_name : Russel, customer_id : 123]
shopping_cart1 = [customer_id : 123, items : [necklace, ring, ear ring], total_price : 2000, discount : 300, price_tobe_paid : 1700]
Crate a few customers and print their information (Personal and shopping info).


"""

class Items():

    # sum the all products total amount
    subtotal = 0

    def __init__ (self, cust_id = 0, product_name = 0, product_price = 0, product_qty = 0, total_price = 0):
        self.cust_id = cust_id
        self.product_name = product_name
        self.product_price = product_price
        self.product_qty = product_qty
        self.total_price = total_price
        self.cart = []


    # calculate the dicsount rate
    def calculate_discount(self):
        
        if Items.subtotal >= 4000:
            return int(Items.subtotal * 0.25)
        
        elif 4000 > Items.subtotal >= 2000:
            return int(Items.subtotal * 0.15)
        
        else:
            return int(Items.subtotal * 0.10)


    # getting purchased items informations from user
    def shopping_cart(self):
  
        while True:

            self.product_name = input("\nPlease type the Product Name: ").capitalize()

            try:

                self.product_price = int(input("Please type the Product Price: "))
                self.product_qty = int(input("Please type the Product Quantity: "))

                # adding every items to the shopping cart
                self.cart.append([self.product_name, self.product_qty, self.product_price])
                print("Products were added to your cart")
                print(self.cart)

            except:
                print("Please type a number!")

            question = input("Press 'n' for finishing your shopping or any to contiue: ").lower()

            self.total_price = self.product_price * self.product_qty
            Items.subtotal += self.total_price

            if question != "n":
                continue
            else:
                # displaying purchased items informations 
                Customer.__str__(self)
                print("\n PRODUCT                       QUANTITY                   PRICE")
                for i in self.cart:
                    print(f"\n {i[0]}                             {i[1]}                      {i[2]} €"
                    "\n")
            
            # get the discount rate
            self.calculate_discount()

            # display the subtotal and discoutn part of the invoice
            self.__str__()
            break


    # calculate the total amount (to paid)
    def get_total_amount(self): 
            price_tobe_paid = Items.subtotal - Items.calculate_discount(self)
            return price_tobe_paid

    # display the subtotal and discoutn part of the invoice
    def __str__(self):
        print ("==================================================================="
              "\nSUBTOTAL                                                  : {} € "
              " \n"
              "\nDISCOUNT                                                  : {} € "
              "\n=================================================================="
              "\n                                                    TOTAL : {} € "
              .format(Items.subtotal, Items.calculate_discount(self),
                      Items.get_total_amount(self)))


class Customer():
    customers = []

    def __init__ (self, cust_name =  "", cust_last_name = "", cust_id = 0):
        self.cust_name = cust_name
        self.cust_last_name = cust_last_name
        self.cust_id = cust_id

    # get the customer informations
    def get_cust_info(self):
        self.cust_name = input("\nPlease type your name: ").capitalize()
        self.cust_last_name = input("Please type your last name: ").upper()
        self.cust_id = input("Please type your id: ")
        Customer.customers.append([self.cust_id, self.cust_name, self.cust_last_name])

    # display the customer informations
    def __str__(self):
        for i in Customer.customers:
            print ("\n                             SHOPPING INVOICE\n"
                "\nCustomer ID : {} "
                  "\nName        : {} "
                  "\nLast Name   : {}"
                  "\n==================================================================\n".format(i[0], i[1], i[2]))


cust_1 = Customer()
cust_1.get_cust_info()

shop_1 = Items()
shop_1.shopping_cart()