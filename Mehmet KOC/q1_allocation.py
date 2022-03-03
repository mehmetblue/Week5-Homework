"""
Question 1:
Create the class Society with following information:
society_name,house_no_of_mem, flat, income

Methods :
An __init__ method to assign initial values of society_name,house_no_of_mem, flat, income
input_data() To read information from members
allocate_flat() To allocate flat according to income using the below table.
show_data() to display the details of the entire class.
![h5](https://user-images.githubusercontent.com/98665012/155852098-3b9c4c90-149e-4685-8cb1-44001a6088bc.png)

"""

class Society():

    # class attribute. Default for every member. 
    # It will change by allocate_flat() method acording to the every member's incom
    flat_type = "A"

    def __init__(self, society_name, house_no_of_mem, flat, income):
        self.society_name = society_name
        self.house_no_of_mem = house_no_of_mem
        self.flat = flat
        self.income = income

    # flat_type will change acroding to the every member's income
    def allocate_flat(self):
        if 25000 <= self.income:
            Society.flat_type = "A"
            return(f"{self.society_name}'s allocated flat type is {self.flat_type}")
        elif 20000 <= self.income < 25000:
            Society.flat_type = "B"
            return(f"{self.society_name}'s allocated flat type is {self.flat_type}")
        elif 15000 <= self.income < 20000:
            Society.flat_type = "C"
            return(f"{self.society_name}'s allocated flat type is {self.flat_type}")
        else:
            Society.flat_type = "D"
            return(f"{self.flat_type}")

    # to show the entire information about the member
    def show_data(self):
        print(f"\n{self.society_name}'s:\nIncome: {self.income}\nHouse Number of Members: {self.house_no_of_mem}\nAllocated Flat Type: {self.allocate_flat()}\n")

# getttin data from user
society_name = input("Please type your Society Name: ")
house_no_of_mem = int(input("Please type your House Number of Members: "))
flat = int(input("Please type your Flat: "))
income = int(input("Please type your Income: "))

# gathering the whole information in one line
mem = Society(society_name, house_no_of_mem, flat, income)

# showing the allacation result and all other information about the member
Society.show_data(mem)