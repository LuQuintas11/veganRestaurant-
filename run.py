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
