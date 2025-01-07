import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('grocery_sample.csv')

# Display the first few rows of the DataFrame
print(df.head())

# define a 'meal' class

class MealType:
    def __init__(self, mealtype: str, calories: int):
        self.mealtype = mealtype
        self.calories = calories

class Food:
    def __init__(self, calories: int):
        self.calories = calories
        self.breakfast = MealType('breakfast', calories * 0.3)
        self.lunch = MealType('lunch', calories * 0.4)
        self.dinner = MealType('dinner', calories * 0.3)

    def get_macros(self, _calories=None):
        if _calories is None:
            _calories = self.calories

        return {
            'protein': int(_calories * 0.3 / 4),
            'fat': int(_calories * 0.2 / 9),
            'carbs': int(_calories* 0.5 / 4),
        }

    def change_meal_calories(self, new_calories: int, mealtype='breakfast'):
        if new_calories > self.calories:
            print('You are trying to add more calories than you should be for the day')
            return
        
        change_calories = self.calories - new_calories
        
        if mealtype == 'breakfast':
            self.bf_calories = new_calories
            self.lunch_calories = change_calories * 0.6
            self.dinner_calories = change_calories * 0.4
        elif mealtype == 'lunch':
            self.lunch_calories = new_calories
            self.bf_calories = change_calories * 0.4
            self.dinner_calories = change_calories * 0.6
        elif mealtype == 'dinner':
            self.dinner_calories = new_calories
            self.bf_calories = change_calories * 0.4
            self.lunch_calories = change_calories * 0.6


    def generate_meal(self, mealtype='breakfast'):
        macros = self.get_macros()

        breakfast = [
            'eggs',
            'bacon',
            'toast'
        ]
        return breakfast
    
    # def generate_lunch(self):
    #     lunch = [
    #         'chicken',
    #         'rice',
    #         'broccoli'
    #     ]
    #     return lunch
    # def generate_dinner(self): 
    #     dinner = [
    #         'steak',
    #         'potatoes',
    #         'asparagus'
    #     ]
    #     return dinner