from unittest import TestCase

from etl.IngredientDigest import IngredientDigest
from etl.InstructionDigest import InstructionDigest
from etl.InstructionGroupDigest import InstructionGroupDigest


class TestInstructionGroupDigest(TestCase):
    instruction_group_digest_id = 123
    instruction_group_number = 9024
    name = "Salad Dressing"

    instruction_digest_id = 910
    step_number = 3
    instruction = "Always wash your hands"

    ingredient_digest_id = 324
    recipe_id = 14
    instruction_group_id = 1244
    food_name = "plain yoghurt"
    description = "Plain Greek Yogurt"
    ingredient_serving_qty = 14
    ingredient_serving_unit = "ounce"
    ingredient_type = "DAIRY"

    def test_add_instruction(self):
        instruction_group_digest = InstructionGroupDigest(self.instruction_group_digest_id,
                                                          self.instruction_group_number,
                                                          self.name)
        instruction_digest = InstructionDigest(self.instruction_digest_id,
                                               self.step_number,
                                               self.instruction)
        instruction_group_digest.add_instruction(instruction_digest)
        self.assertEqual(instruction_digest, instruction_group_digest.instructions[0])
        print(instruction_group_digest)

    def test_add_ingredient(self):
        instruction_group_digest = InstructionGroupDigest(self.instruction_group_digest_id,
                                                          self.instruction_group_number,
                                                          self.name)

        ingredient = IngredientDigest(self.ingredient_digest_id,
                                      self.recipe_id,
                                      self.instruction_group_id,
                                      self.food_name,
                                      self.description,
                                      self.ingredient_serving_qty,
                                      self.ingredient_serving_unit,
                                      self.ingredient_type)
        instruction_group_digest.add_ingredient(ingredient)

        self.assertEqual(ingredient, instruction_group_digest.ingredients[0])
        print(instruction_group_digest)
