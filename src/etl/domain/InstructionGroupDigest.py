from dataclasses import dataclass, field
from typing import List

from src.etl.domain.IngredientDigest import IngredientDigest
from src.etl.domain.InstructionDigest import InstructionDigest


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
        for instructions in self.instructions:
            text = text + "\n   " + str(instructions) + ","
        text = text + "]"

        text = text + ", ingredients ["
        for ingredient in self.ingredients:
            text = text + "\n   " + str(ingredient) + ","
        text = text + "]"

        return text.format(self.instruction_group_number, self.name)

    def to_json_dictionary(self):
        json = {
            "instructionGroupNumber": self.instruction_group_number,
            "name": self.name,
            "instructions": [],
            "ingredients": []
        }
        for instruction in self.instructions:
            if isinstance(instruction, InstructionDigest):
                json["instructions"].append(instruction.to_json_dictionary())
        for ingredient in self.ingredients:
            if isinstance(ingredient, IngredientDigest):
                json["ingredients"].append(ingredient.to_json_dictionary())

        return json
