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


USER_OPTIONS = """
Choose an option, 1 or 2:
    1. Vegan.
    2. Vegeterian.
"""


def parse_menu(worksheet):
    """
    Parse values from the different worksheets and create a dict with them
    """
    menu_category_dict = defaultdict(list)
    for row in worksheet[1:]:
        menu_category_dict[row[0]].append(row)
    return menu_category_dict


def validate_order(category_input, DISH_CATEGORY_MAP):
    """
    Validate data from category_input
    """
    if category_input in DISH_CATEGORY_MAP.keys():
        return True


def order_menu(worksheet, data):
    """
    Functions that show the menua and take order from user input
    """
    DISH_CATEGORY_MAP = parse_menu(worksheet)
    print("Type what you would prefer:")
    category_input = (input(tabulate([DISH_CATEGORY_MAP.keys()]))).upper()
    while not validate_order(category_input, DISH_CATEGORY_MAP):
        print("Choose from the different categories: Salad, Pizza or Burger")
        category_input = (input(tabulate([DISH_CATEGORY_MAP.keys()]))).upper()
    category_dishes = DISH_CATEGORY_MAP[category_input]
    category = tabulate(category_dishes, showindex=range(1, (len(category_dishes)+1)))
    print(category)
    while True:
        try:
            order = int(input("Type dish number that you'd like to order"))
            if order > len(DISH_CATEGORY_MAP[category_input]):
                continue
        except ValueError:
            continue
        break
    order_dish = DISH_CATEGORY_MAP[category_input][order-1]
    
    print("This is what you choose:")
    print(f"{tabulate([order_dish])}")
    data.append(order_dish[0:2])

    print("This is your complete order")
    print(f"{tabulate(data[1:])}")

    return data


def update_worksheet(data):
    """
    Function that update "orders" worksheet
    """
    SHEET.worksheet("orders").insert_rows(data)


def validate_data(user_name):
    """
    Function that validate data from user_name input
    """
    is_valid_name = user_name.isalpha()

    if not is_valid_name:

        print("Type a valid name")

    return is_valid_name


def main():
    """
    Get name and order input from user
    """
    print("Welcome to Happy Cow Restaurant")
    print("Everything is vegan or vegeterian and definitely delicious.")
    print("We offer Salads, Burgers and Pizzas.")
    user_name = input("Please tell us your name:")

    while not validate_data(user_name):

        user_name = input("What is your name:")

    print(f"Hello {user_name}. We are ready to take your order!")

    data.append([user_name])
    while True:
        try:
            user_input = int(input(USER_OPTIONS))
        except ValueError:
            user_input = None
        if user_input == 1:
            print("Check our menu:")
            print(tabulate(VEGAN, tablefmt="simple"))
            order_menu(VEGAN, data)
        elif user_input == 2:
            print("Check our menu:")
            print(tabulate(VEGETERIAN, tablefmt='simple'))
            order_menu(VEGETERIAN, data)
        else:
            print("Choose option 1 for Vegan or option 2 for Vegeterian")
            continue
        another_order = input("Do you want to order anything else? (Y/N)")
        if another_order.upper() != "Y":
            update_worksheet(data)
            print(f"This is your order {user_name}:")
            print(f"{tabulate(data[1:])}")
            print("We are preparing your food.Thank you for choosing us")
            break
if __name__ == "__main__":
    main()

