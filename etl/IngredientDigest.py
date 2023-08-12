from dataclasses import dataclass


@dataclass
class IngredientDigest:
    food_name: str
    description: str
    ingredient_serving_qty: float
    ingredient_serving_unit: str
    ingredient_type: str

    def __str__(self):
        text = ("IngredientDigest: food_name='{}', description='{}', ingredient_serving_qty={}"
                ", ingredient_serving_unit={}, ingredient_type='{}'")
        return text.format(self.food_name,
                           self.description,
                           self.ingredient_serving_qty,
                           self.ingredient_serving_unit,
                           self.ingredient_type)

    def to_json_dictionary(self):
        json = {
            "foodName": self.food_name,
            "description": self.description,
            "ingredientServingQty": self.ingredient_serving_qty,
            "ingredientServingUnit": self.ingredient_serving_unit,
            "ingredientType": self.ingredient_type
        }

        return json
