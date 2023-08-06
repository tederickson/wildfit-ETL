from etl.IngredientDigest import IngredientDigest
from etl.InstructionDigest import InstructionDigest


class InstructionGroupDigest:
    def __init__(self,
                 instruction_group_number,
                 name):
        self.instruction_group_number = instruction_group_number
        self.name = name
        self.instructions = []
        self.ingredients = []

    def add_instruction(self, instruction):
        self.instructions.append(instruction)

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def __str__(self):
        text = "InstructionGroupDigest: instruction_group_number={}, name='{}'"
        text = text + ", instructions ["
        for x in self.instructions:
            text = text + "\n   " + str(x) + ","
        text = text + "]"

        text = text + ", ingredients ["
        for x in self.ingredients:
            text = text + "\n   " + str(x) + ","
        text = text + "]"

        return text.format(self.instruction_group_number, self.name)

    def to_json_dictionary(self):
        json = {
            "instructionGroupNumber": self.instruction_group_number,
            "name": self.name,
            "instructions": [],
            "ingredients": []
        }
        for x in self.instructions:
            if isinstance(x, InstructionDigest):
                json["instructions"].append(x.to_json_dictionary())
        for x in self.ingredients:
            if isinstance(x, IngredientDigest):
                json["ingredients"].append(x.to_json_dictionary())

        return json
