from unittest import TestCase

from etl.RecipeColumn import RecipeColumn


class TestRecipeColumn(TestCase):
    def test_from_heading(self):
        self.assertEqual(RecipeColumn.TITLE, RecipeColumn.from_heading('Title'))
        self.assertEqual(RecipeColumn.DESCRIPTION, RecipeColumn.from_heading('Description'))

    def test_from_heading_unknown_value(self):
        self.assertEqual(None, RecipeColumn.from_heading('Bob'))
