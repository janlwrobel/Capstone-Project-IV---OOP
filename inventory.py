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
class Shoe:
    """
    Represents a shoe object with attributes such as country, code, product, cost, and quantity.
    """
    def __init__(self, country, code, product, cost, quantity):
        """
        Initialise attributes of the Shoe class with provided parameters:
           - country: str
           - code: str
           - product: str
           - cost: float
           - quantity: int
        """
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity


    def get_cost(self):
        """
        Represents a shoe object with attributes such as country, code, product, cost, and quantity.
        """
        return self.cost


    def get_quantity(self):
        """
        Return the quantity of the shoe object
        """
        return self.quantity


    def __str__(self):
        """
        Override the default __str__ method to return a string representation of a shoe object
        """
        return f'{self.country},{self.code},{self.product},{self.cost},{self.quantity}'


# ═════════════════════ Functions ═════════════════════
def read_shoes_data():
    """
    This function reads the data from the file 'inventory.txt', and creates a Shoe object with this data
    by assigning individual comma-separated values to the corresponding Shoe attributes.
    It then appends the created Shoe object into the shoe_list.
    """
    try:
        with open('inventory.txt', 'r') as read_file_txt:
            content_of_file = read_file_txt.readlines()[1:]  # [1:] Skipping first line of the txt file (Headers).
            for line in content_of_file:
                # Skipping 'empty lines' to prevent error from trying to load an empty line to variable 'country'
                if line == '\n':
                    continue
                # Assigning individual comma-separated values to the corresponding Shoe attributes.
                country, code, product, cost, quantity = line.strip("\n").split(",")
                # Creating a Shoe object and placing it in the shoe_list.
                shoe_list.append(Shoe(country, code, product, int(cost), int(quantity)))
    except FileNotFoundError as error_fnfe:
        # Handling file not found error using try-except block
        print("─────────────────────────────────────────────────────────")
        print(f"{RED}The file that you are trying to open does not exist.{WHITE}")
        print(f"{RED}{error_fnfe}{WHITE}")
        print("─────────────────────────────────────────────────────────")
    except Exception as error_exc:
        # Handling file not found error using try-except block
        print("─────────────────────────────────────────────────────────")
        print(f"{RED}Reading data from file error.{WHITE}")
        print(f"{RED}{error_exc}{WHITE}")
        print("─────────────────────────────────────────────────────────")


def capture_shoes():
    """
    This function allows the user to capture data about a shoe by taking input from the console,
    and uses this data to create a Shoe object and appends this object inside the shoe list.
    """
    main_menu_bool = False # Flag to check if user wants to continue
    while not main_menu_bool:
        # Take input from the user for each Shoe attribute
        user_input_country = input("Enter a country: ")
        user_input_code = input("Enter an order code: ")
        user_input_product = input("Enter a product name: ")

        # Exception handling for integer cost value, prevents string entry
        while True:
            try:
                user_input_cost = int(input("Enter cost: "))
                break
            except ValueError:
                print(f"{RED}Wrong input. Please enter a number.{WHITE}")

        # Exception handling for integer quantity value, prevents string entry
        while True:
            try:
                user_input_quantity = int(input("Enter a quantity: "))
                break
            except ValueError:
                print(f"{RED}Wrong input. Please enter a number.{WHITE}")

        # Ask the user if they want to add the Shoe object to the shoe list
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
                # Create a Shoe object with user input values and append it to the shoe list
                shoe_list.append(Shoe(user_input_country, user_input_code, user_input_product,
                                      user_input_cost, user_input_quantity))
                print("─────────────────────────────────────────────────────────")
                print(f"{GREEN}New inventory object has been added to the shoe_list{WHITE}")
                print("─────────────────────────────────────────────────────────")
                # Exit from mine while loop.
                main_menu_bool = True
                break
            elif user_input_chose == '2':
                # User chose not to add the object to the shoe list
                print("─────────────────────────────────────────────────────────")
                print(f"{YELLOW}Adding an entry to the database has been cancelled.{WHITE}")
                print("─────────────────────────────────────────────────────────")
                # Exit from mine while loop.
                main_menu_bool = True
                break
            elif user_input_chose == '3':
                # User chose to enter the data again
                break
            else:
                print("─────────────────────────────────────────────────────────")
                print(f"{RED}Wrong input. Please try again.{WHITE}")
                print("─────────────────────────────────────────────────────────")


def view_all():
    """
    This function iterates over the shoe_list and extracts the attributes of each Shoe object.
    It then places these attributes as a list into a temporary 2D list called temp_tabulate_list.
    This list is used to print the data using the tabulate module.
    """
    # Create a temporary empty list to store Shoe object attributes
    temp_tabulate_list = []

    # Create a temporary empty list to store Shoe object attributes
    for shoe in shoe_list:
        # Append the attributes of the Shoe object as a list to the temporary list
        temp_tabulate_list.append([shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity])

    # Use the tabulate module to print the data in a formatted table
    print(tabulate(temp_tabulate_list, headers=["Country", "Code", "Product", "Cost", "Quantity"], tablefmt="pretty"))



def re_stock():
    """
    This function finds the shoe object with the lowest quantity,
    which is the shoes that need to be restocked. It then asks the user if
    they want to add additional stock to the product and updates the
    corresponding object in the shoe_list. Finally, it updates the
    new_inventory.txt file with the updated shoe list and creates a backup
    of the original file.

    The min() function is used to find the object with the lowest quantity
    in shoe_list. A lambda function is used as the 'key' argument in the
    min() function to find the lowest quantity in the shoe_list.
    """
    # Find the Shoe object with the lowest quantity in shoe_list
    lowest_quantity_restock = min(shoe_list, key=lambda shoe: shoe.quantity)

    # Printing product name with the lowest quantity
    print("─────────────────────────────────────────────────────────")
    print(f"The smallest stock level is on {BOLD}{lowest_quantity_restock.product}{WHITE}"
          f" ({RED}{lowest_quantity_restock.quantity}{WHITE}).")
    print("─────────────────────────────────────────────────────────")

    # Ask the user if they want to add additional stock to the product
    user_to_answer = input(f"Would you like to add additional stock to {lowest_quantity_restock.product}"
                           f" ({YELLOW}Y{WHITE}es / {YELLOW}N{WHITE}o)?: ").upper()

    if user_to_answer == 'Y' or user_to_answer == 'YES':
        # Ask the user how much stock they want to add
        while True:
            try:
                user_to_restock = int(input("How much would you add to the current stock?: "))
                lowest_quantity_restock.quantity += user_to_restock
                break
            except ValueError:
                print("─────────────────────────────────────────────────────────")
                print(f"{RED}Wrong input. Please try again.{WHITE}")
                print("─────────────────────────────────────────────────────────")

        # Update the new_inventory.txt file with the updated shoe_list
        with open('new_inventory.txt', 'w') as to_file:
            # Write the first row of the file - headers
            to_file.write("Country,Code,Product,Cost,Quantity\n")
            # Write each Shoe object in shoe_list to the new file
            for shoe in shoe_list:
                to_file.writelines(shoe.__str__() + "\n")

        # Backup the original file using the back_up_files() function
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
   This function searches for a shoe object in the shoe_list based on the product code
   entered by the user. If the code is found during the for loop, the object is returned
   in string form to the print() function. If the object is not in the list, a message
   is displayed, and the user is asked if they want to try again. If not, an abort message
   is returned.

   :return: A string representation of the product found by product code.
   :return: An abandon message as a string.
   """
    while True:
        # Prompt user for product code input
        product_code = input("Please enter a product code: ").strip().upper()
        # Search for product code in the shoe_list and return the object as a string
        for shoe in shoe_list:
            if shoe.code == product_code:
                return (f'''─────────────────────────────────────────────────────────
{GREEN}{shoe}{WHITE}
─────────────────────────────────────────────────────────''')
        # If the product code is not found, display a message and ask the user if they want to try again
        print("─────────────────────────────────────────────────────────")
        print(f"{RED}Product code {WHITE}{BOLD}{product_code}{WHITE}{RED} "
              f"not found in database{WHITE}.")
        print("─────────────────────────────────────────────────────────")
        user_re_enter = input(f"Would you like to try again ({YELLOW}Y{WHITE}es / {YELLOW}N{WHITE}o)?: ").upper()
        # If the user wants to try again, repeat the process
        if user_re_enter == 'Y' or user_re_enter == 'YES':
            pass
        # If the user does not want to try again, return an abandon message
        else:
            return (f'''─────────────────────────────────────────────────────────
{YELLOW}Procedure abandoned, return to Main Menu.{WHITE}
─────────────────────────────────────────────────────────''')


def value_per_item():
    """
    This function calculates the total value for each item in the shoe_list, using the formula:
    value = cost * quantity. It then prints the calculation on the console for all shoes using the
    'tabulate' module (https://pypi.org/project/tabulate/).

    :return: None
    """
    while True:
        user_chose = input(f"Do you want to calculate the total value for each item "
                           f"({YELLOW}Y{WHITE}es / {YELLOW}N{WHITE}o)?: ").upper()
        if user_chose == 'Y' or user_chose == 'YES':
            # Temporary list for values - for tabulate module
            temp_tabulate_list = []
            # Loop through the shoe_list, calculate the total value, and add to temporary list.
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
    This function determines the product with the highest quantity and prints the shoe as being for sale.
    The max() function is used to find the object with the highest quantity in shoe_list. A lambda function is used
    as the 'key' argument in the max() function to find the highest quantity in the shoe_list. Then, the name of
    the product with the highest quantity is printed on the console, along with its quantity and the message
    that it can be set for sale.
    """
    highest_quantity_sale = max(shoe_list, key=lambda shoe: shoe.quantity)
    print("─────────────────────────────────────────────────────────")
    print(f"{BOLD}{highest_quantity_sale.product} with quantity of {highest_quantity_sale.quantity} "
          f"can be set for {YELLOW}Sale{WHITE}.")
    print("─────────────────────────────────────────────────────────")



def back_up_files():
    """
    Improves the safety of working with the 'inventory.txt' file by creating backup files.
    First, a new file named 'new_inventory.txt' is created, which contains the new inventory data.
    The function then checks if the new file exists and is not empty. If it is, it renames the original
    'inventory.txt' file to 'old_inventory.txt' and renames the new file to 'inventory.txt'.
    If the old backup file 'old_inventory.txt' exists, it is removed.
    Note: This function assumes that the 'inventory.txt' file already exists and that the function that writes
    to it creates a new file named 'new_inventory.txt'.
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
