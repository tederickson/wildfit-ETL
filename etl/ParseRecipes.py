import os
import openpyxl

from etl.RecipeDigest import RecipeDigest

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


def get_value(row, column_names, column_name):
    index = column_names.index(column_name)
    return row[index].value


def parse_recipe_title_sheet(recipe_sheet) -> RecipeDigest:
    validate_column_names(TITLE_COLUMNS, recipe_sheet)
    first_row = recipe_sheet[2]

    recipe_digest = RecipeDigest(-1,
                                 get_value(first_row, TITLE_COLUMNS, 'Title'),
                                 get_value(first_row, TITLE_COLUMNS, 'Season'),
                                 get_value(first_row, TITLE_COLUMNS, 'PrepTimeMinutes'),
                                 get_value(first_row, TITLE_COLUMNS, 'CookTimeMinutes'),
                                 get_value(first_row, TITLE_COLUMNS, 'ServingUnit'),
                                 get_value(first_row, TITLE_COLUMNS, 'ServingQty'),
                                 get_value(first_row, TITLE_COLUMNS, 'Introduction'))
    return recipe_digest


def parse_recipe_sheet(recipe_sheet):
    validate_column_names(RECIPE_COLUMNS, recipe_sheet)


def parse_recipe(recipe_file):
    print(recipe_file)
    wb = openpyxl.load_workbook(RECIPE_DIRECTORY + recipe_file)
    validate_sheet_names(wb.sheetnames)
    recipe_digest = parse_recipe_title_sheet(wb[TITLE_SHEET])
    print(recipe_digest)
    parse_recipe_sheet(wb[RECIPE_SHEET])


if __name__ == '__main__':
    recipe_list = os.listdir(RECIPE_DIRECTORY)

    for recipe in recipe_list:
        parse_recipe(recipe)
