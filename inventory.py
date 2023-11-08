
#==============Import========================
import math
#========The beginning of the class==========
# Defined a class for shoe objects
class Shoe:
# Intinizialising attrributes for the shoe object
    def __init__(self, country, code, product, cost, qauntity):                
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.qauntity = qauntity

# Method that will get the cost of the shoe               
    def get_cost(self):                                                              
        cost_shoe = self.cost
        return cost_shoe

# Method that will get the amount of that certain shoe
    def get_quantity(self):                                            
        qauntity_shoe = self.qauntity
        return qauntity_shoe        

# Using string method to print out each shoe object's data 
    def __str__(self):                                                 
        return print(f"The shoe,{self.product},is from {self.country} and it's code is {self.code}. The amount in stock is {self.qauntity} and the cost is {self.cost}\n")

        
#================Shoe list================
shoe_list = []                                      # Empty list to add the shoe objects                                                     
#==========Functions outside the class==============
def read_shoes_data():
# Used try-except to see if the file exist
    while True:
        try:
            file_open = open("inventory.txt","r+")
        except FileNotFoundError as error:
            print("The file does not exist.")
            print(error)
        finally:
            lines = file_open.readlines()[1::]# Using this functiom to use lines only after the first line                     
            for line in lines:
                shoe_line = line.split(",")   # Split each line in commas                                                 
                shoe = Shoe(shoe_line[0],shoe_line[1],shoe_line[2],shoe_line[3],shoe_line[4].strip("\n"))
                shoe_list.append(shoe)        # Append each shoe object to a shoe_list
            file_open.close() 
            return shoe_list
# This function will allow a user to capture data about a shoe                          
def capture_shoes():                
    # Asking user for certian attributes so that I can add it to the list:
    choice_country = input("Enter the country the shoe came from:")
    choice_code = input("Enter the code of the shoe:")
    choice_product = input("Enter the produces the shoe:")
    choice_cost = input("Enter the cost of the shoe:")
    choice_qauntity = input("Enter the qauntity of the shoe:")
    
    # Append the object inside the shoe list
    shoe = Shoe(choice_country,choice_code,choice_product,choice_cost,choice_qauntity)
    shoe_list.append(shoe)
    
    # Append to the file
    with open("inventory.txt","a") as f:
        f.write(f"\n{choice_country},{choice_code},{choice_product},{choice_cost},{choice_qauntity}")
        
def view_all():
    # Looping through each item in the list, printing the shoe object out as a string
    for item in shoe_list: 
        item.__str__()

# This function will find the shoe object with the lowest quantity   
def re_stock():
    shoe_qauntity_list = []                     # Created a empty list
    for item in shoe_list:
        shoe_qauntity = int(item.qauntity)      # Using the qauntity method for the qauntity of the shoe
        shoe_qauntity_list.append(shoe_qauntity)# Appending each shoe qauntity to a list        
        
    shoe_qauntity_list.sort()                   # Sorts the qauntity list    
    min_num = min(shoe_qauntity_list)           # Mininum value of the qauntity list
    # Asking user if they want to change the qauntity of the list
    update_qauntity = input("Want to change the lowest qauntity of the shoe? Yes/ No :").lower()
    
    # If-statement is used to see if user's choice is "YES"
    if update_qauntity == "yes":
        item_list = []                          # Empty list to add items
        # Asking user what number they want to replace the lowest qauntity with
        replace_qauntity = input("Enter the amount you want to change?")
        # For-loop is used to loop through each item in the shoe-list
        for item in shoe_list:
            # If the item qauntity is eqaul to lowest qauntity
            if int(item.qauntity) == min_num:  
                # This function will replace the lowest qauntity with user's choice
                item.qauntity = replace_qauntity
            
            # New variable to turn data to a string
            items_shoe = f"""{item.country},{item.code},{item.product},{item.cost},{item.qauntity}"""
            item_list.append(items_shoe)
        
        # Join the items in the items shoe list      
        items_shoes = '\n'.join(item_list)     
        # Open the inventory file and overwrite it so that the new update can be made
        with open("inventory.txt","w") as o:
            o.write(f"Country,Code,Product,Cost,Quantity \n")
            o.write(f"{items_shoes}")
            
# This function will search for a shoe from the list using the shoe code                                                                     
def search_shoe():
    # Asking for user for the code of the shoe                                                                            
    looking_for_shoe = input("What is the code of the shoe  you looking for? ")              
    
    # Using a for-loop to loop through each item in the shoe list
    for item in shoe_list:
    # If the that certain item's code is eqaul to the user's code                                                                   
        if item.code == looking_for_shoe:
        # Print out shoe object as a string                                             
           print(item.__str__())

# This function will calculate the total value for each item   
def value_per_item():                                                                  
    for item in shoe_list:
        # Calculate the total value for each item
        value = int(item.cost) * int(item.qauntity)
        # Print this information on the console for all the shoes                                  
        print(f"{item.product} : {int(item.cost)} * {int(item.qauntity)} = {value}")    

# This function get the most qauntity shoe 
def highest_qty():                                                      
    shoe_qauntity_list = []                     # Used a empty list for each shoe qauntity
    for item in shoe_list:                      # Looped through each item and adding it to the empty list
        shoe_qauntity = int(item.qauntity)
        shoe_qauntity_list.append(shoe_qauntity)
             
    shoe_qauntity_list.sort()    
    max_num = max(shoe_qauntity_list)           # Using the max function to get the maxinum value in the list
    for shoe_item in shoe_list:
        if int(shoe_item.qauntity) == max_num:
            print(f"The largest qauntity shoe is : {item.product}")

#==========List insert=================
read_shoes_data()
#==========Main Menu=============
# Created a menu that executes each function above

while True:
    ask_user = int(input("""Enter any number below to do the folowing:" 
                     1  : Capture a new shoe
                     2  : Search for a certian shoe
                     3  : Restock the lowest quantity
                     4  : View all the shoes
                     5  : Get the value for each item
                     6  : Highest qauntity
                     7  : Exit 
                     : """))
    
    if ask_user == 1:
        capture_shoes()
    elif ask_user == 2:
        search_shoe()
    elif ask_user == 3:
        re_stock()
    elif ask_user == 4:
        view_all()
    elif ask_user == 5:
        value_per_item()
    elif ask_user == 6:
        highest_qty()
    elif ask_user == 7:
        print("Goodbye fellow user!")
        exit()
    else:
        print("You entered the wrong value please try again")   
    
           
    
        



