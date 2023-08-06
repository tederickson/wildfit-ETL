from etl.AbstractParseSheet import AbstractParseSheet
from etl.RecipeDigest import RecipeDigest
from etl.TitleColumn import TitleColumn


class ParseTitleSheet(AbstractParseSheet):
    HEADERS = ['Season', 'Title', 'Introduction', 'PrepTimeMinutes', 'CookTimeMinutes', 'ServingQty',
               'ServingUnit']

    def get_headers(self):
        return self.HEADERS

    def validate_headers(self, sheet):
        index = 0
        for column in sheet.iter_cols():
            if self.HEADERS[index] != column[0].value:
                raise Exception("Expected column {} instead of {}".format(self.HEADERS[index], column[0].value))
            index += 1

    def get_value(self, row, column_name):
        index = TitleColumn.from_heading(column_name).value
        return row[index].value

    def parse_sheet(self, sheet):
        self.validate_headers(sheet)
        first_row = sheet[2]

        recipe_digest = RecipeDigest(self.get_value(first_row, 'Title'),
                                     self.get_value(first_row, 'Season'),
                                     self.get_value(first_row, 'PrepTimeMinutes'),
                                     self.get_value(first_row, 'CookTimeMinutes'),
                                     self.get_value(first_row, 'ServingUnit'),
                                     self.get_value(first_row, 'ServingQty'),
                                     self.get_value(first_row, 'Introduction'))
        return recipe_digest
