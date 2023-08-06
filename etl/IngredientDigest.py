class IngredientDigest:
    def __init__(self,
                 food_name,
                 description,
                 ingredient_serving_qty,
                 ingredient_serving_unit,
                 ingredient_type):
        self.food_name = food_name
        self.description = description
        self.ingredient_serving_qty = ingredient_serving_qty
        self.ingredient_serving_unit = ingredient_serving_unit
        self.ingredient_type = ingredient_type

    def __str__(self):
        text = ("IngredientDigest: food_name='{}', description='{}', ingredient_serving_qty={}"
                ", ingredient_serving_unit={}, ingredient_type='{}'")
        return text.format(self.food_name,
                           self.description,
                           self.ingredient_serving_qty,
                           self.ingredient_serving_unit,
                           self.ingredient_type)
