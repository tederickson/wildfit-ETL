class IngredientDigest:
    def __init__(self,
                 ingredient_digest_id,
                 recipe_id,
                 instruction_group_id,
                 food_name,
                 description,
                 ingredient_serving_qty,
                 ingredient_serving_unit,
                 ingredient_type):
        self.ingredient_digest_id = ingredient_digest_id
        self.recipe_id = recipe_id
        self.instruction_group_id = instruction_group_id
        self.food_name = food_name
        self.description = description
        self.ingredient_serving_qty = ingredient_serving_qty
        self.ingredient_serving_unit = ingredient_serving_unit
        self.ingredient_type = ingredient_type

    def __str__(self):
        text = ("IngredientDigest: id={}, recipe_id={}, instruction_group_id={}"
                ", food_name='{}', description='{}', ingredient_serving_qty={}"
                ", ingredient_serving_unit={}, ingredient_type='{}'")
        return text.format(self.ingredient_digest_id,
                           self.recipe_id,
                           self.instruction_group_id,
                           self.food_name,
                           self.description,
                           self.ingredient_serving_qty,
                           self.ingredient_serving_unit,
                           self.ingredient_type)
