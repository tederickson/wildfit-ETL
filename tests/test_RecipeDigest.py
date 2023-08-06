from unittest import TestCase

from etl.InstructionGroupDigest import InstructionGroupDigest
from etl.RecipeDigest import RecipeDigest


class TestRecipeDigest(TestCase):
    name = "Tuna Salad"
    season = "SPRING"
    prep_time_min = 15
    cook_time_min = 0
    serving_unit = "serving"
    serving_qty = 4
    introduction = "We love this!"

    def test_strip_whitespace(self):
        recipe = RecipeDigest(self.name + "  ",
                              self.season + "  ",
                              self.prep_time_min,
                              self.cook_time_min,
                              self.serving_unit + "  ",
                              self.serving_qty,
                              self.introduction + "  ")

        self.assertEqual(self.name, recipe.name)
        self.assertEqual(self.season, recipe.season)
        self.assertEqual(self.serving_qty, recipe.serving_qty)
        self.assertEqual(self.introduction, recipe.introduction)
        self.assertEqual(0, len(recipe.instruction_groups))

    def test_add_instruction_group(self):
        recipe = RecipeDigest(self.name,
                              self.season,
                              self.prep_time_min,
                              self.cook_time_min,
                              self.serving_unit,
                              self.serving_qty,
                              self.introduction)
        self.assertEqual(self.name, recipe.name)
        self.assertEqual(0, len(recipe.instruction_groups))

        instruction_group = InstructionGroupDigest(15, "Salad")
        recipe.add_instruction_group(instruction_group)
        self.assertEqual(1, len(recipe.instruction_groups))

    def test_to_string(self):
        recipe = RecipeDigest(self.name,
                              self.season,
                              self.prep_time_min,
                              self.cook_time_min,
                              self.serving_unit,
                              self.serving_qty,
                              self.introduction)
        text = str(recipe)
        self.assertIn("season", text)

    def test_to_json_create_recipe(self):
        recipe = RecipeDigest(self.name,
                              self.season,
                              self.prep_time_min,
                              self.cook_time_min,
                              self.serving_unit,
                              self.serving_qty,
                              self.introduction)

        instruction_group = InstructionGroupDigest(15, "Salad")
        recipe.add_instruction_group(instruction_group)

        dictionary = recipe.to_json_dictionary()

        self.assertTrue('id' not in dictionary)
        self.assertEqual(self.name, dictionary['name'])
        self.assertEqual(self.season, dictionary['season'])
        self.assertEqual(self.prep_time_min, dictionary['prepTimeMin'])
        self.assertEqual(self.serving_unit, dictionary['servingUnit'])
        self.assertTrue(1, len(dictionary['instructionGroups']))
