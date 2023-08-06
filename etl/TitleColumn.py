from enum import Enum


class TitleColumn(Enum):
    SEASON = 0
    TITLE = 1
    INTRODUCTION = 2
    PREP_TIME_MINUTES = 3
    COOK_TIME_MINUTES = 4
    SERVING_QTY = 5
    SERVING_UNIT = 6

    @classmethod
    def from_heading(cls, name):
        match name:
            case 'Season':
                return cls.SEASON
            case 'Title':
                return cls.TITLE
            case 'Introduction':
                return cls.INTRODUCTION
            case 'PrepTimeMinutes':
                return cls.PREP_TIME_MINUTES
            case 'CookTimeMinutes':
                return cls.COOK_TIME_MINUTES
            case 'ServingQty':
                return cls.SERVING_QTY
            case 'ServingUnit':
                return cls.SERVING_UNIT
