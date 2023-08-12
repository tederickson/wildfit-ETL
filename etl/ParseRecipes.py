import json
import os
import sys
import getopt
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
DEBUG = False


def validate_sheet_names(sheet_names):
    if len(sheet_names) != 2:
        raise Exception("Expected two sheets")
    expected = [TITLE_SHEET, RECIPE_SHEET]
    if sheet_names != expected:
        raise Exception("Expected sheet names {} instead of {}".format(expected, sheet_names))


def is_new_recipe(recipe_digest):
    url = HOST_SERVER + "/v1/recipes/seasons/" + recipe_digest.season + "/names/" + recipe_digest.name
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("{} failed.  Response is {}".format(url, response))

    response_dictionary = response.json()
    existing_recipes = response_dictionary.get('recipes')

    return len(existing_recipes) == 0


def create_recipe(recipe_digest):
    url = HOST_SERVER + "/v1/recipes/users/" + UUID
    json_dictionary = recipe_digest.to_json_dictionary()
    write_to_server_test_directory(json_dictionary, recipe_digest)

    response = requests.post(url, json=json_dictionary)

    if response.status_code != 200:
        print(f"Status Code: {response.status_code}, Response: {response.json()}")
        raise Exception(response.json())


def write_to_server_test_directory(json_dictionary, recipe_digest):
    if DEBUG:
        print(f"writing {recipe_digest.name}")
        file_name = "../../wildfit-server/src/test/resources/" + recipe_digest.name + ".json"
        file_name = file_name.replace(" ", "_")

        with open(file_name, 'w') as f:
            json.dump(json_dictionary, f, indent=2)


def parse_recipe(recipe_file):
    print(recipe_file)
    wb = openpyxl.load_workbook(RECIPE_DIRECTORY + recipe_file)
    validate_sheet_names(wb.sheetnames)

    parse_title_sheet = ParseTitleSheet()
    parse_recipe_sheet = ParseRecipeSheet()

    recipe_digest = parse_title_sheet.parse_sheet(wb[TITLE_SHEET])

    if is_new_recipe(recipe_digest):
        parse_recipe_sheet.parse_sheet(wb[RECIPE_SHEET], recipe_digest)
        create_recipe(recipe_digest)


if __name__ == '__main__':
    UUID = os.environ.get('UUID')
    if UUID is None:
        raise Exception("UUID environment variable is not defined")

    HOST_SERVER = os.environ.get('host-server')
    if HOST_SERVER is None:
        raise Exception("host-server environment variable is not defined")

    argv = sys.argv[1:]
    opts, args = getopt.getopt(argv, "hd", ["help", "debug"])
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("ParseRecipes.py --debug  or -d")
            print("Debug writes the JSON request to the local server test directory")
            sys.exit()
        elif opt in ("-d", "--debug"):
            DEBUG = True

    recipe_list = os.listdir(RECIPE_DIRECTORY)

    for recipe in recipe_list:
        parse_recipe(recipe)
