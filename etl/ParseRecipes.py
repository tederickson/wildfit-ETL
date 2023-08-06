import os
import openpyxl
import requests
import urllib.parse
from dotenv import load_dotenv
from etl.RecipeDigest import RecipeDigest
from etl.TitleColumn import TitleColumn

load_dotenv()  # take environment variables from .env.

RECIPE_DIRECTORY = "../data/"
TITLE_SHEET = 'Sheet1'
RECIPE_SHEET = 'Sheet2'

TITLE_COLUMNS = ['Season',
                 'Title',
                 'Introduction',
                 'PrepTimeMinutes',
                 'CookTimeMinutes',
                 'ServingQty',
                 'ServingUnit']

RECIPE_COLUMNS = ['Title', 'Instruction', 'Text', 'Ingredient', 'Food', 'Description', 'Quantity', 'Unit', 'Type']
UUID = ""
HOST_SERVER = ""


def validate_sheet_names(sheet_names):
    if len(sheet_names) != 2:
        raise Exception("Expected two sheets")
    expected = [TITLE_SHEET, RECIPE_SHEET]
    if sheet_names != expected:
        raise Exception("Expected sheet names {} instead of {}".format(expected, sheet_names))


def validate_column_names(expected, sheet):
    index = 0
    for column in sheet.iter_cols():
        if expected[index] != column[0].value:
            raise Exception("Expected column {} instead of {}".format(expected[index], column[0].value))
        index += 1


def get_value(row, column_name):
    index = TitleColumn.from_heading(column_name).value
    return row[index].value


def parse_recipe_title_sheet(recipe_sheet):
    validate_column_names(TITLE_COLUMNS, recipe_sheet)
    first_row = recipe_sheet[2]

    recipe_digest = RecipeDigest(get_value(first_row, 'Title'),
                                 get_value(first_row, 'Season'),
                                 get_value(first_row, 'PrepTimeMinutes'),
                                 get_value(first_row, 'CookTimeMinutes'),
                                 get_value(first_row, 'ServingUnit'),
                                 get_value(first_row, 'ServingQty'),
                                 get_value(first_row, 'Introduction'))
    return recipe_digest


def parse_recipe_sheet(recipe_digest, recipe_sheet):
    validate_column_names(RECIPE_COLUMNS, recipe_sheet)


def is_new_recipe(recipe_digest):
    safe_string = urllib.parse.quote_plus(recipe_digest.name)
    url = HOST_SERVER + "/v1/recipes/seasons/" + recipe_digest.season + "/names/" + safe_string
    response = requests.get(url)

    return response.status_code == 404


def parse_recipe(recipe_file):
    print(recipe_file)
    wb = openpyxl.load_workbook(RECIPE_DIRECTORY + recipe_file)
    validate_sheet_names(wb.sheetnames)
    recipe_digest = parse_recipe_title_sheet(wb[TITLE_SHEET])
    print(recipe_digest)

    if is_new_recipe(recipe_digest):
        parse_recipe_sheet(recipe_digest, wb[RECIPE_SHEET])


if __name__ == '__main__':
    UUID = os.environ.get('UUID')
    if UUID is None:
        raise Exception("UUID environment variable is not defined")

    HOST_SERVER = os.environ.get('host-server')
    if HOST_SERVER is None:
        raise Exception("host-server environment variable is not defined")

    recipe_list = os.listdir(RECIPE_DIRECTORY)

    for recipe in recipe_list:
        parse_recipe(recipe)
