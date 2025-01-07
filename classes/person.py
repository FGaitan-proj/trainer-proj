class Person:
    def __init__(self, age: int, sex: str, weight: int, height: int, activity_level: int):
        self.age = age
        self.sex = sex
        self.height = height # in inches
        self.weight = weight # in lbs
        # self.body_fat = body_fat
        self.activity_level = activity_level
        self.maintanence_cals = self.calculate_maintanence_calories()
        self.old_weight = []
        self.old_height = []

    def get_maintanence_calories(self):
        return self.maintanence_cals
    
    def update_weight(self, new_weight: int):
        self.weight = new_weight
        self.old_weight.append(new_weight)

        return self.weight
    
    def update_height(self, new_height: int):
        self.height = new_height
        self.old_height.append(new_height)

        return self.weight
    
    def calculate_maintanence_calories(self):
        if self.sex == 'male':
            self.BMR = 10 * self.weight + 6.25 * self.height - 5 * self.age + 5
        else:
            self.BMR = 10 * self.weight + 6.25 * self.height - 5 * self.age - 161

        if self.activity_level == 2:
            return self.BMR * 1.375
        elif self.activity_level == 3:
            return self.BMR * 1.55
        elif self.activity_level == 4:
            return self.BMR * 1.725
        elif self.activity_level == 5:
            return self.BMR * 1.9
        else:
            return self.BMR * 1.2

    def calculate_daily_macros(self, measure='calories'):
        if measure == 'calories':
            return {
                'protein': int(self.get_maintanence_calories() * 0.3 / 4),
                'fat': int(self.get_maintanence_calories() * 0.2 / 9),
                'carbs': int(self.get_maintanence_calories() * 0.5 / 4),
                'measure': 'calories'
            }
        elif measure == 'grams':
            return {
                'protein': int(self.weight * 2.2),
                'fat': int(self.weight * 0.45),
                'carbs': int(self.weight * 3.5),
                'measure': 'grams'
            }