from enum import Enum


class RecipeColumn(Enum):
    TITLE = 0
    INSTRUCTION = 1
    TEXT = 2
    INGREDIENT = 3
    FOOD = 4
    DESCRIPTION = 5
    QUANTITY = 6
    UNIT = 7
    TYPE = 8

    @classmethod
    def from_heading(cls, name):
        match name:
            case 'Title':
                return cls.TITLE
            case 'Instruction':
                return cls.INSTRUCTION
            case 'Text':
                return cls.TEXT
            case 'Ingredient':
                return cls.INGREDIENT
            case 'Food':
                return cls.FOOD
            case 'Description':
                return cls.DESCRIPTION
            case 'Quantity':
                return cls.QUANTITY
            case 'Unit':
                return cls.UNIT
            case 'Type':
                return cls.TYPE
