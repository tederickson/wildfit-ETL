class RecipeDigest:
    JSON_RECIPE_ID = "id"
    JSON_NAME = "name"
    JSON_SEASON = "season"
    JSON_PREP_TIME_MIN = "prepTimeMin"
    JSON_COOK_TIME_MIN = "cookTimeMin"
    JSON_SERVING_UNIT = "servingUnit"
    JSON_SERVING_QTY = "servingQty"
    JSON_INTRODUCTION = "introduction"

    def __init__(self,
                 name,
                 season,
                 prep_time_min,
                 cook_time_min,
                 serving_unit,
                 serving_qty,
                 introduction):
        self.recipe_id = 0
        self.name = str(name).strip()
        self.season = str(season).strip()
        self.prep_time_min = prep_time_min
        self.cook_time_min = cook_time_min
        self.serving_unit = str(serving_unit).strip()
        self.serving_qty = serving_qty
        self.introduction = str(introduction).strip()
        self.instruction_groups = []

    def add_instruction_group(self, instruction_group):
        self.instruction_groups.append(instruction_group)

    def __str__(self):
        text = ("RecipeDigest: recipe_id={}, name='{}', season={}, prepTimeMin={}, cookTimeMin={},"
                " servingUnit='{}', servingQty={}, introduction='{}', instruction_groups [")

        for x in self.instruction_groups:
            text = text + "\n   " + str(x) + ","
        text = text + "]"

        return text.format(self.recipe_id,
                           self.name,
                           self.season,
                           self.prep_time_min,
                           self.cook_time_min,
                           self.serving_unit,
                           self.serving_qty,
                           self.introduction)

    # Convert class to JSON for /v1/recipes/users/{userId}
    def to_json_create_recipe(self):
        json = {
            self.JSON_NAME: self.name,
            self.JSON_SEASON: self.season,
            self.JSON_PREP_TIME_MIN: self.prep_time_min,
            self.JSON_COOK_TIME_MIN: self.cook_time_min,
            self.JSON_SERVING_UNIT: self.serving_unit,
            self.JSON_SERVING_QTY: self.serving_qty,
            self.JSON_INTRODUCTION: self.introduction
        }

        return json
