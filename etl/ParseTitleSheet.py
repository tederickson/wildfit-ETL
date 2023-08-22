from etl.AbstractParseSheet import AbstractParseSheet
from etl.RecipeDigest import RecipeDigest
from etl.TitleColumn import TitleColumn


class ParseTitleSheet(AbstractParseSheet):
    HEADERS = ['Season', 'Title', 'Introduction', 'PrepTimeMinutes', 'CookTimeMinutes', 'ServingQty',
               'ServingUnit', 'Photo']

    def get_headers(self):
        return self.HEADERS

    def validate_headers(self, sheet):
        index = 0
        for column in sheet.iter_cols():
            if self.HEADERS[index] != column[0].value:
                raise Exception("Expected column {} instead of {}".format(self.HEADERS[index], column[0].value))
            index += 1

    def get_value(self, row, column):
        return row[column.value].value

    def parse_sheet(self, sheet):
        self.validate_headers(sheet)
        first_row = sheet[2]

        recipe_digest = RecipeDigest(self.get_value(first_row, TitleColumn.TITLE),
                                     self.get_value(first_row, TitleColumn.SEASON),
                                     self.get_value(first_row, TitleColumn.PREP_TIME_MINUTES),
                                     self.get_value(first_row, TitleColumn.COOK_TIME_MINUTES),
                                     self.get_value(first_row, TitleColumn.SERVING_UNIT),
                                     self.get_value(first_row, TitleColumn.SERVING_QTY),
                                     self.get_value(first_row, TitleColumn.INTRODUCTION),
                                     self.get_value(first_row, TitleColumn.PHOTO))
        return recipe_digest
