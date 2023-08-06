import os
import urllib.parse

import openpyxl
import requests
from dotenv import load_dotenv

from etl.ParseRecipeSheet import ParseRecipeSheet
from etl.ParseTitleSheet import ParseTitleSheet

load_dotenv()  # obtain environment variables from .env.

RECIPE_DIRECTORY = "../data/"
TITLE_SHEET = 'Sheet1'
RECIPE_SHEET = 'Sheet2'

UUID = ""
HOST_SERVER = ""


def validate_sheet_names(sheet_names):
    if len(sheet_names) != 2:
        raise Exception("Expected two sheets")
    expected = [TITLE_SHEET, RECIPE_SHEET]
    if sheet_names != expected:
        raise Exception("Expected sheet names {} instead of {}".format(expected, sheet_names))


def is_new_recipe(recipe_digest):
    safe_string = urllib.parse.quote_plus(recipe_digest.name)
    url = HOST_SERVER + "/v1/recipes/seasons/" + recipe_digest.season + "/names/" + safe_string
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("{} failed.  Response is {}".format(url, response))

    response_dictionary = response.json()
    existing_recipes = response_dictionary.get('recipes')

    return len(existing_recipes) == 0


def parse_recipe(recipe_file):
    print(recipe_file)
    wb = openpyxl.load_workbook(RECIPE_DIRECTORY + recipe_file)
    validate_sheet_names(wb.sheetnames)

    parse_title_sheet = ParseTitleSheet()
    parse_recipe_sheet = ParseRecipeSheet()

    recipe_digest = parse_title_sheet.parse_sheet(wb[TITLE_SHEET])
    print(recipe_digest)

    if is_new_recipe(recipe_digest):
        parse_recipe_sheet.parse_sheet(wb[RECIPE_SHEET], recipe_digest)
        print(recipe_digest)


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
