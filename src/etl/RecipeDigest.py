from src.etl.InstructionGroupDigest import InstructionGroupDigest


class RecipeDigest:

    def __init__(self,
                 name,
                 season,
                 prep_time_min,
                 cook_time_min,
                 serving_unit,
                 serving_qty,
                 introduction,
                 photo):
        self.name = str(name).strip()
        self.season = str(season).strip()
        self.prep_time_min = prep_time_min
        self.cook_time_min = cook_time_min
        self.serving_unit = str(serving_unit).strip()
        self.serving_qty = serving_qty
        self.introduction = str(introduction).strip()
        self.photo = str(photo).strip()
        self.instruction_groups = []

    def add_instruction_group(self, instruction_group):
        self.instruction_groups.append(instruction_group)

    def __str__(self):
        text = ("RecipeDigest: name='{}', season={}, prepTimeMin={}, cookTimeMin={},"
                " servingUnit='{}', servingQty={}, introduction='{}',photo='{}', instruction_groups [")

        for x in self.instruction_groups:
            text = text + "\n   " + str(x) + ","
        text = text + "]"

        return text.format(self.name,
                           self.season,
                           self.prep_time_min,
                           self.cook_time_min,
                           self.serving_unit,
                           self.serving_qty,
                           self.photo,
                           self.introduction)

    # Convert class to dictionary for /v1/recipes/users/{userId}
    def to_json_dictionary(self):
        json = {
            "name": self.name,
            "season": self.season,
            "prepTimeMin": self.prep_time_min,
            "cookTimeMin": self.cook_time_min,
            "servingUnit": self.serving_unit,
            "servingQty": self.serving_qty,
            "introduction": self.introduction,
            "thumbnail": self.photo,
            "recipeGroups": []
        }

        for x in self.instruction_groups:
            if isinstance(x, InstructionGroupDigest):
                json["recipeGroups"].append(x.to_json_dictionary())

        return json
