class RecipeDigest:
    def __init__(self,
                 recipe_id,
                 name,
                 season,
                 prep_time_min,
                 cook_time_min,
                 serving_unit,
                 serving_qty,
                 introduction):
        self.recipe_id = recipe_id
        self.name = name
        self.season = season
        self.prep_time_min = prep_time_min
        self.cook_time_min = cook_time_min
        self.serving_unit = serving_unit
        self.serving_qty = serving_qty
        self.introduction = introduction
        self.instruction_groups = []

    def add_instruction_group(self, instruction_group):
        self.instruction_groups.append(instruction_group)

    def __str__(self):
        text = ("RecipeDigest: recipe_id={}, name='{}', season={}, prepTimeMin={}, cookTimeMin={},"
                " servingUnit='{}', servingQty={}, introduction='{}', instruction_groups [")

        for x in self.instruction_groups:
            text = text + "\n" + str(x) + ","
        text = text + "]"

        return text.format(self.recipe_id,
                           self.name,
                           self.season,
                           self.prep_time_min,
                           self.cook_time_min,
                           self.serving_unit,
                           self.serving_qty,
                           self.introduction)
