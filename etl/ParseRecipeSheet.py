from etl.AbstractParseSheet import AbstractParseSheet
from etl.RecipeColumn import RecipeColumn
from etl.RecipeDigest import RecipeDigest


class ParseRecipeSheet(AbstractParseSheet):
    HEADERS = ['Title', 'Instruction', 'Text', 'Ingredient', 'Food', 'Description', 'Quantity', 'Unit', 'Type']

    def get_headers(self):
        return self.HEADERS

    def validate_headers(self, sheet):
        index = 0
        for column in sheet.iter_cols():
            if self.HEADERS[index] != column[0].value:
                raise Exception("Expected column {} instead of {}".format(self.HEADERS[index], column[0].value))
            index += 1

    def get_value(self, row, column_name):
        index = RecipeColumn.from_heading(column_name).value
        return row[index].value

    def parse_sheet(self, sheet, recipe_digest):
        self.validate_headers(sheet)

        return recipe_digest
