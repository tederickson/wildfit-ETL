from unittest import TestCase
from etl.RecipeDigest import RecipeDigest
from etl.InstructionGroupDigest import InstructionGroupDigest


class TestRecipeDigest(TestCase):
    digest_id = 1230
    name = "Tuna Salad"
    season = "SPRING"
    prep_time_min = 15
    cook_time_min = 0
    serving_unit = 4
    serving_qty = "serving"
    introduction = "We love this!"

    def test_add_instruction_group(self):
        recipe = RecipeDigest(self.digest_id,
                              self.name,
                              self.season,
                              self.prep_time_min,
                              self.cook_time_min,
                              self.serving_unit,
                              self.serving_qty,
                              self.introduction)
        self.assertEqual(self.name, recipe.name)
        self.assertEqual(0, len(recipe.instruction_groups))

        instruction_group = InstructionGroupDigest(5, 15, "Salad")
        recipe.add_instruction_group(instruction_group)
        self.assertEqual(1, len(recipe.instruction_groups))

    def test_to_string(self):
        recipe = RecipeDigest(self.digest_id,
                              self.name,
                              self.season,
                              self.prep_time_min,
                              self.cook_time_min,
                              self.serving_unit,
                              self.serving_qty,
                              self.introduction)
        text = str(recipe)
        self.assertIn("recipe_id", text)

    def test_to_json_create_recipe(self):
        recipe = RecipeDigest(self.digest_id,
                              self.name,
                              self.season,
                              self.prep_time_min,
                              self.cook_time_min,
                              self.serving_unit,
                              self.serving_qty,
                              self.introduction)

        instruction_group = InstructionGroupDigest(5, 15, "Salad")
        recipe.add_instruction_group(instruction_group)

        dictionary = recipe.to_json_create_recipe()

        self.assertTrue('id' not in dictionary)
        self.assertEqual(self.name, dictionary['name'])
        self.assertEqual(self.season, dictionary['season'])
        self.assertEqual(self.prep_time_min, dictionary['prepTimeMin'])
        self.assertEqual(self.serving_unit, dictionary['servingUnit'])
        self.assertTrue('instructionGroups' not in dictionary)
