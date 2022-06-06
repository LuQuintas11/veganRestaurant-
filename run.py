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


def parse_menu(worksheet_data):
    """
    Parse values from the different worksheets and create a dict with them
    """
    menu_category_dict = defaultdict(list)
    for row in worksheet_data[1:]:
        menu_category_dict[row[0]].append(row)
    return menu_category_dict
DISH_CATEGORY_MAP = parse_menu(VEGAN)







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
            print(tabulate(VEGAN, tablefmt='grid'))
            order_menu(VEGAN, data)
            parse_menu(VEGAN)
        elif data_menu == 2:
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