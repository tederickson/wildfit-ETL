from unittest import TestCase

from etl.TitleColumn import TitleColumn


class TestTitleColumn(TestCase):
    def test_from_heading(self):
        self.assertEqual(TitleColumn.TITLE, TitleColumn.from_heading('Title'))
        self.assertEqual(TitleColumn.COOK_TIME_MINUTES, TitleColumn.from_heading('CookTimeMinutes'))

    def test_from_heading_unknown_value(self):
        self.assertEqual(None, TitleColumn.from_heading('Bob'))
