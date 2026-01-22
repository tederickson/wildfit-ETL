from unittest import TestCase

from src.etl.domain.IngredientDigest import IngredientDigest
from src.etl.domain.InstructionDigest import InstructionDigest
from src.etl.domain.InstructionGroupDigest import InstructionGroupDigest


class TestInstructionGroupDigest(TestCase):
    instruction_group_number = 9024
    name = "Salad Dressing"

    step_number = 3
    instruction = "Always wash your hands"

    food_name = "plain yoghurt"
    description = "Plain Greek Yogurt"
    ingredient_serving_qty = 14
    ingredient_serving_unit = "ounce"
    ingredient_type = "DAIRY"

    def test_add_instruction(self):
        instruction_group_digest = InstructionGroupDigest(self.instruction_group_number, self.name)
        instruction_digest = InstructionDigest(self.step_number, self.instruction)
        instruction_group_digest.add_instruction(instruction_digest)
        self.assertEqual(instruction_digest, instruction_group_digest.instructions[0])
        print(instruction_group_digest)

    def test_add_ingredient(self):
        instruction_group_digest = InstructionGroupDigest(self.instruction_group_number, self.name)

        ingredient = IngredientDigest(self.food_name,
                                      self.description,
                                      self.ingredient_serving_qty,
                                      self.ingredient_serving_unit,
                                      self.ingredient_type)
        instruction_group_digest.add_ingredient(ingredient)

        self.assertEqual(ingredient, instruction_group_digest.ingredients[0])
        print(instruction_group_digest)
