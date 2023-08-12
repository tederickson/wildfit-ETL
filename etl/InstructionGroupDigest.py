from etl.IngredientDigest import IngredientDigest
from etl.InstructionDigest import InstructionDigest
from dataclasses import dataclass, field
from typing import List


@dataclass
class InstructionGroupDigest:
    instruction_group_number: int
    name: str
    instructions: List[InstructionDigest] = field(default_factory=lambda: [])
    ingredients: List[IngredientDigest] = field(default_factory=lambda: [])

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
