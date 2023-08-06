from enum import Enum


class RecipeColumn(Enum):
    TITLE = 0
    INSTRUCTION = 1
    TEXT = 2
    INGREDIENT = 3
    DESCRIPTION = 4
    QUANTITY = 5
    UNIT = 6
    TYPE = 7

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
            case 'Description':
                return cls.DESCRIPTION
            case 'Quantity':
                return cls.QUANTITY
            case 'Unit':
                return cls.UNIT
            case 'Type':
                return cls.TYPE
