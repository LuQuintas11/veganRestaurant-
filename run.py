import gspread
from google.oauth2.service_account import Credentials
from tabulate import tabulate
from collections import defaultdict

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("menu")
VEGAN_DATA = SHEET.worksheet("vegan")
VEGAN = VEGAN_DATA.get_all_values()
VEGETERIAN_DATA = SHEET.worksheet("vegeterian")
VEGETERIAN = VEGETERIAN_DATA.get_all_values()

data = []


def parse_menu(worksheet_data):
    """
    Parse values from the different worksheets and create a dict with them
    """
    menu_category_dict = defaultdict(list)
    for row in worksheet_data[1:]:
        menu_category_dict[row[0]].append(row)
    return menu_category_dict
DISH_CATEGORY_MAP = parse_menu(VEGAN)


USER_OPTIONS = """
Choose an option, 1 or 2:
    1. Vegan
    2. Vegeterian.
"""


def validate_order(category_input):
    """
    Validate data from category_input
    """
    if category_input in DISH_CATEGORY_MAP.keys():
        return True


def order_menu(worksheet, data):
    """
    Functions that show the menua and take order from user input
    """
    print("Type what you would prefer:")
    category_input = (input(tabulate([DISH_CATEGORY_MAP.keys()]))).upper()
    while not validate_order(category_input):
        print("Choose from the different categories: Salad, Pizza or Burger")
        category_input = (input(tabulate([DISH_CATEGORY_MAP.keys()]))).upper()
    category_dishes = DISH_CATEGORY_MAP[category_input]
    category = tabulate(category_dishes, showindex=range(1, (len(category_dishes)+1)))
    print(category)
    if category_input == "SALAD":
        while True:
            try:
                order = int(input("Type dish number that you'd like to order"))
                if order > len(DISH_CATEGORY_MAP[category_input]):
                    print(category)
                    continue
            except ValueError:
                print(category)
                continue
            break
        salad_dish = DISH_CATEGORY_MAP[category_input][order-1]
        print("This is what you choose:")
        print(f"{tabulate([salad_dish])} ")
        data.append(salad_dish[0:2])
    elif category_input == "PIZZA":
        while True:
            try:
                order = int(input("Type dish number that you'd like to order"))
                if order > len(DISH_CATEGORY_MAP[category_input]):
                    print(category)
                    continue
            except ValueError:
                print(category)
                continue
            break
        pizza_dish = DISH_CATEGORY_MAP[category_input][order-1]
        print("This is what you choose:")
        print(f"{tabulate([pizza_dish])} ")
        data.append(pizza_dish[0:2])
    elif category_input == "BURGER":
        while True:
            try:
                order = int(input("Type dish number that you'd like to order"))
                if order > len(DISH_CATEGORY_MAP[category_input]):
                    print(category)
                    continue
            except ValueError:
                print(category)
                continue
            break
        burger_dish = DISH_CATEGORY_MAP[category_input][order - 1]
        print("This is what you choose:")
        print(f"{tabulate([burger_dish])} ")
        data.append(burger_dish[0:2])
    
    print("This is your complete order")
    print(f"{tabulate(data[1:])}")
    return data


def update_worksheet(data):
    """
    Function that update "orders" worksheet
    """
    SHEET.worksheet("orders").insert_rows(data)


def validate_data(data_name):
    """
    Function that validate data from data_name input
    """
    is_valid_name = data_name.isalpha()

    if not is_valid_name:

        print("Type a valid name")

    return is_valid_name


def main():
    """
    Get name and order input from user
    """
    print("Welcome to The Sunshine Inn.")
    print("Everything is vegan/vegeterian and definitely delicious.")
    data_name = input("Please tell us your name:")

    while not validate_data(data_name):

        data_name = input("What is your name:")

    print(f"Hello {data_name}. We are ready to take your order!")

    data.append([data_name])
    while True:
        try:
            data_menu = int(input(USER_OPTIONS))
        except ValueError:
            data_menu = None
        if data_menu == 1:
            print("Check our menu:")
            print(tabulate(VEGAN))
            order_menu(VEGAN, data)
            parse_menu(VEGAN)
        elif data_menu == 2:
            print("Check our menu:")
            print(tabulate(VEGETERIAN, tablefmt='grid'))
            order_menu(VEGETERIAN, data)
            parse_menu(VEGETERIAN)
        else:
            print("Choose option 1 for Vegan or option 2 for Vegeterian")
            continue
        another_order = input("Do you want to order anything else? (Y/N)")
        if another_order.upper() != "Y":
            update_worksheet(data)
            print(f"This is your order {data_name}:")
            print(f"{tabulate(data[1:])}")
            print("Thank you for choosing us")
            break
if __name__ == "__main__":
    main()