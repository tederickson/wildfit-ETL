from dataclasses import dataclass


@dataclass
class IngredientDigest:
    food_name: str
    description: str
    ingredient_serving_qty: float
    ingredient_serving_unit: str
    ingredient_type: str

    def to_json_dictionary(self):
        json = {
            "foodName": self.food_name,
            "description": self.description,
            "ingredientServingQty": self.ingredient_serving_qty,
            "ingredientServingUnit": self.ingredient_serving_unit,
            "ingredientType": self.ingredient_type
        }

        return json
