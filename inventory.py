'''
╔═══════════════ HyperionDev - DfE Software Engineering December - Bootcamp ══════════════╗
║####                         Jan Lukasz Wrobel - JL22110005141                       ####║
║####                                Capstone Project IV —                            ####║
║####                                  Object-Oriented                                ####║
║####                                    Programming                                  ####║
╚═════════════════════════════════════════════════════════════════════════════════════════╝'''
# Require to install tabulate library from - https://pypi.org/project/tabulate/
# pip install tabulate
from tabulate import tabulate
# os module, for further operations on back_up files.
import os

# ═════════════════════ Variables ═════════════════════
shoe_list = []  # The list will be used to store a list of objects of shoes.
# Colours
WHITE = '\033[0m'
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BOLD = '\033[1m'


# ══════════════════════ Class ════════════════════════
"""

"""
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''

    def get_cost(self):
        """
        :return: Cost of the object
        """
        return self.cost


    def get_quantity(self):
        """
        :return: Quantity of the object
        """
        return self.quantity


    def __str__(self):
        """
        :return: String representation of a class
        """
        return f'{self.country},{self.code},{self.product},{self.cost},{self.quantity}'


# ═════════════════════ Functions ═════════════════════
def read_shoes_data():
    """
    This function will open the file inventory.txt and read the data from this file,
    then create a shoes object with this data and append this object into the shoes list.
    One line in this file represents data to create one object of shoes.
    """
    try:
        with open('inventory.txt', 'r') as read_file_txt:
            content_of_file = read_file_txt.readlines()[1:]  # [1:] Skipping first line of the txt file.
            for line in content_of_file:
                # Skipping 'empty lines' - preventing from error which my occur from trying
                # to load empty line to variable 'country'
                if line == '\n':
                    continue
                # Assignment of individual comma-separated values
                # to the corresponding variable names Classy Shoe.
                country, code, product, cost, quantity = line.strip("\n").split(",")
                # Creating an object and placing it in the shoe_list.
                shoe_list.append(Shoe(country, code, product, int(cost), int(quantity)))
    except FileNotFoundError as error_fnfe:
        print("─────────────────────────────────────────────────────────")
        print(f"{RED}The file that you are trying to open does not exist.{WHITE}")
        print(f"{RED}{error_fnfe}{WHITE}")
        print("─────────────────────────────────────────────────────────")
    except Exception as error_exc:
        print("─────────────────────────────────────────────────────────")
        print(f"{RED}Reading data from file error.{WHITE}")
        print(f"{RED}{error_exc}{WHITE}")
        print("─────────────────────────────────────────────────────────")


def capture_shoes():
    """
    This function will allow a user to capture data about a shoe and use this data
    to create a shoe object and append this object inside the shoe list.
    """
    main_menu_bool = False
    while not main_menu_bool:
        user_input_country = input("Enter a country: ")
        user_input_code = input("Enter an order code: ")
        user_input_product = input("Enter a product name: ")
        # Exception handling for integer cost value. Prevent from string entry
        while True:
            try:
                user_input_cost = int(input("Enter cost: "))
                break
            except ValueError:
                print(f"{RED}Wrong input. Please enter a number.{WHITE}")
        # Exception handling for integer quantity value. Prevent from string entry
        while True:
            try:
                user_input_quantity = int(input("Enter a quantity: "))
                break
            except ValueError:
                print(f"{RED}Wrong input. Please enter a number.{WHITE}")
        # Checking statement before adding object to shoe_list.
        while True:
            user_input_chose = input(f'''─────────────────────────────────────────────────────────
{YELLOW}{user_input_country},{user_input_code},{user_input_product},{user_input_cost},{user_input_quantity}{WHITE}
─────────────────────────────────────────────────────────
Do you want to add the created item to the list?
{YELLOW}1{WHITE} - Yes
{YELLOW}2{WHITE} - No
{YELLOW}3{WHITE} - Enter the data again
=> ''')
            if user_input_chose == '1':
                shoe_list.append(Shoe(user_input_country, user_input_code, user_input_product,
                                      user_input_cost, user_input_quantity))
                print("─────────────────────────────────────────────────────────")
                print(f"{GREEN}New inventory object has been added to the shoe_list{WHITE}")
                print("─────────────────────────────────────────────────────────")
                # Exit from mine while loop.
                main_menu_bool = True
                break
            elif user_input_chose == '2':
                print("─────────────────────────────────────────────────────────")
                print(f"{YELLOW}Adding an entry to the database has been cancelled.{WHITE}")
                print("─────────────────────────────────────────────────────────")
                # Exit from mine while loop.
                main_menu_bool = True
                break
            elif user_input_chose == '3':
                break
            else:
                print("─────────────────────────────────────────────────────────")
                print(f"{RED}Wrong input. Please try again.{WHITE}")
                print("─────────────────────────────────────────────────────────")


def view_all():
    """
    https://pypi.org/project/tabulate/

    First we create a temporary empty list 'temp_tabulate_list', then we use a for loop
    that reads each object in the 'shoe_list' and extract from each object
    its attributes and place them as a list into the temp_tabulate_list. This creates a 2d list
    temp_tabulate_list = []
    """
    temp_tabulate_list = []
    for shoe in shoe_list:
        temp_tabulate_list.append([shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity])
    # Printing data using tabulate module
    print(tabulate(temp_tabulate_list, headers=["Country", "Code", "Product", "Cost", "Quantity"], tablefmt="pretty"))



def re_stock():
    """
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked.

    min() function to find the object with the lowest quantity in shoe_list.
    Lambda function is used as the 'key' argument in the min() function to find lowest quantity
    in the shoe_list
    """

    lowest_quantity_restock = min(shoe_list, key=lambda shoe: shoe.quantity)
    # Printing product name with the lowest quantity
    print("─────────────────────────────────────────────────────────")
    print(f"The smallest stock level is on {BOLD}{lowest_quantity_restock.product}{WHITE}"
          f" ({RED}{lowest_quantity_restock.quantity}{WHITE}).")
    print("─────────────────────────────────────────────────────────")
    user_to_answer = input(f"Would you like to add additional stock to {lowest_quantity_restock.product}"
                           f" ({YELLOW}Y{WHITE}es / {YELLOW}N{WHITE}o)?: ").upper()
    if user_to_answer == 'Y' or user_to_answer == 'YES':
        # Exception handling for integer input.
        while True:
            try:
                user_to_restock = int(input("How much would you add to the current stock?: "))
                lowest_quantity_restock.quantity += user_to_restock
                break
            except ValueError:
                print("─────────────────────────────────────────────────────────")
                print(f"{RED}Wrong input. Please try again.{WHITE}")
                print("─────────────────────────────────────────────────────────")
        # Creating new file with write only attribute
        with open('new_inventory.txt', 'w') as to_file:
            # First row of the file - headers.
            to_file.write("Country,Code,Product,Cost,Quantity\n")
            # For loop for re-writing shoe_list content to new file.
            for shoe in shoe_list:
                to_file.writelines(shoe.__str__() + "\n")
        # Safety function for file backup.
        back_up_files()
        print("─────────────────────────────────────────────────────────")
        print(f"{GREEN}Item restocked successfully.{WHITE}")
        print("─────────────────────────────────────────────────────────")
    else:
        print("─────────────────────────────────────────────────────────")
        print(f"{YELLOW}Procedure abandoned, return to Main Menu.{WHITE}")
        print("─────────────────────────────────────────────────────────")


def search_shoe():
    """
    This function is responsible for finding items in the shoe_list based on the code
    entered by the user. If the code is found during a for loop, the object is returned in string
    form to the print() function. If the object is not in the list, a message is displayed, and user
    is asked if he wants to try again. If not, an abort message is returned.

    :return: Product string representation found by product code
    :return: String abandon message.
    """

    while True:
        product_code = input("Please enter a product code: ").strip().upper()
        # for loop, looking for product code and returning it as a string
        for shoe in shoe_list:
            if shoe.code == product_code:
                return (f'''─────────────────────────────────────────────────────────
{GREEN}{shoe}{WHITE}
─────────────────────────────────────────────────────────''')
        # Writing a message if item is not in the list
        print("─────────────────────────────────────────────────────────")
        print(f"{RED}Product code {WHITE}{BOLD}{product_code}{WHITE}{RED} "
              f"not found in database{WHITE}.")
        print("─────────────────────────────────────────────────────────")
        # Asking a user for:
        user_re_enter = input(f"Would you like to try again ({YELLOW}Y{WHITE}es / {YELLOW}N{WHITE}o)?: ").upper()
        if user_re_enter == 'Y' or user_re_enter == 'YES':
            pass
        # Returning a abandon message.
        else:
            return (f'''─────────────────────────────────────────────────────────
{YELLOW}Procedure abandoned, return to Main Menu.{WHITE}
─────────────────────────────────────────────────────────''')


def value_per_item():
    """
    https://pypi.org/project/tabulate/

    This function will calculate the total value for each item.
    Formula for Total value: value = cost * quantity.
    Print calculations on the console for all the shoes.
    """
    while True:
        user_chose = input(f"Do you want to calculate the total value for each item "
                           f"({YELLOW}Y{WHITE}es / {YELLOW}N{WHITE}o)?: ").upper()
        if user_chose == 'Y' or user_chose == 'YES':
            # Temporary list for values - for tabulate module
            temp_tabulate_list = []
            # For loop for calculation and adding values to temporary list
            for shoe in shoe_list:
                value = shoe.get_cost() * shoe.get_quantity()
                temp_tabulate_list.append([shoe.product, shoe.get_cost(), shoe.get_quantity(), "-", value])
            # Printing data using tabulate module
            print(tabulate(temp_tabulate_list, headers=["Product", "Cost", "Qty", "-", "Total Value"], tablefmt="pretty"))
            break
        elif user_chose == 'N' or user_chose == 'NO':
            print("─────────────────────────────────────────────────────────")
            print(f"{YELLOW}Procedure abandoned, return to Main Menu.{WHITE}")
            print("─────────────────────────────────────────────────────────")
            break
        else:
            print("─────────────────────────────────────────────────────────")
            print(f"{RED}Wrong input. Please try again.{WHITE}")
            print("─────────────────────────────────────────────────────────")


def highest_qty():
    """
    Function determine the product with the highest quantity and
    print this shoe as being for sale.

    max() function to find the object with the highest quantity in shoe_list.
    Lambda function is used as the 'key' argument in the max() function to find the highest quantity
    in the shoe_list.
    """
    highest_quantity_sale = max(shoe_list, key=lambda shoe: shoe.quantity)
    print("─────────────────────────────────────────────────────────")
    print(f"{BOLD}{highest_quantity_sale.product} with quantity of {highest_quantity_sale.quantity} "
          f"can be set for {YELLOW}Sale{WHITE}.")
    print("─────────────────────────────────────────────────────────")



def back_up_files():
    """
     This function is responsible for improving safety when the programme works with the inventory.txt file
     The file is not overwritten immediately after the changes. Only a new file named 'new_inventory.txt' is created.
     The function checks if the newly created file exists, if so it checks if the file is not empty
     (if the file size is different from zero). Then replaces the inventory.txt file for old_inventory.txt, and the
     new_inventory file.txt for inventory.txt. If all goes well, the function deletes the old file.
    """
    new_backup_file = "new_inventory.txt"
    old_backup_file = "old_inventory.txt"
    if os.path.exists(new_backup_file):
        if os.path.getsize(new_backup_file) != 0:
            os.rename("inventory.txt", "old_inventory.txt")
            os.rename("new_inventory.txt", "inventory.txt")
        else:
            os.remove('new_inventory.txt')

    if os.path.exists(old_backup_file):
        os.remove("old_inventory.txt")


# ═════════════════════ Main Menu ═════════════════════
# Reading from inventory.txt to the shoe_list.
read_shoes_data()

while True:
    user_choice = input(f'''What would you like to do:
{YELLOW}1{WHITE} - Add new item to database.
{YELLOW}2{WHITE} - Show all items.
{YELLOW}3{WHITE} - Cheng stock level of the item.
{YELLOW}4{WHITE} - Search item by his code.
{YELLOW}5{WHITE} - Show total value per item.
{YELLOW}6{WHITE} - Show item with highest quantity

{YELLOW}0{WHITE} - Quit
=>  ''')
    if user_choice == '1':
        capture_shoes()
    elif user_choice == '2':
        view_all()
    elif user_choice == '3':
        re_stock()
    elif user_choice == '4':
        print(search_shoe())
    elif user_choice == '5':
        value_per_item()
    elif user_choice == '6':
        highest_qty()
    elif user_choice == '0':
        print("Good bye!")
        quit()
    else:
        print("─────────────────────────────────────────────────────────")
        print(f"{RED}Wrong input. Please try again.{WHITE}")
        print("─────────────────────────────────────────────────────────")
