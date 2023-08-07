from etl.AbstractParseSheet import AbstractParseSheet
from etl.IngredientDigest import IngredientDigest
from etl.InstructionDigest import InstructionDigest
from etl.InstructionGroupDigest import InstructionGroupDigest
from etl.RecipeColumn import RecipeColumn


class ParseRecipeSheet(AbstractParseSheet):
    HEADERS = ['Title', 'Instruction', 'Text', 'Ingredient', 'Description', 'Quantity', 'Unit', 'Type']

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
        instruction_group_number = 0
        recipe_row = 2
        row = sheet[recipe_row]
        title = self.get_value(row, 'Title')
        if title is None:
            instruction_group_digest = InstructionGroupDigest(instruction_group_number, "")
            self.add_instruction(instruction_group_digest, row)
        else:
            instruction_group_digest = InstructionGroupDigest(instruction_group_number, title)

        for recipe_row in range(3, sheet.max_row + 1):
            row = sheet[recipe_row]
            title = self.get_value(row, 'Title')
            instruction = self.get_value(row, 'Instruction')
            # ingredient = self.get_value(row, 'Ingredient')
            # print("Title {} Instruction {} Ingredient {}".format(title, instruction, ingredient))

            if title is not None:
                recipe_digest.add_instruction_group(instruction_group_digest)
                instruction_group_number += 1
                instruction_group_digest = InstructionGroupDigest(instruction_group_number, title)
            elif instruction is not None:
                self.add_instruction(instruction_group_digest, row)
            else:
                self.add_ingredient(instruction_group_digest, row)

        recipe_digest.add_instruction_group(instruction_group_digest)

        return recipe_digest

    def add_instruction(self, instruction_group_digest, row):
        instruction_digest = InstructionDigest(self.get_value(row, 'Instruction'),
                                               self.get_value(row, 'Text'))
        instruction_group_digest.add_instruction(instruction_digest)

    def add_ingredient(self, instruction_group_digest, row):
        ingredient_digest = IngredientDigest(self.get_value(row, 'Ingredient'),
                                             self.get_value(row, 'Description'),
                                             self.get_value(row, 'Quantity'),
                                             self.get_value(row, 'Unit'),
                                             self.get_value(row, 'Type'))
        instruction_group_digest.add_ingredient(ingredient_digest)
