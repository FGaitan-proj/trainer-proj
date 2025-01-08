import unittest
from classes.person import Person
from classes.trainer import Trainer
from classes.workout_draft import Exercise, Workout

# Import your functions here
# from your_module import add, subtract, multiply, divide

class TestMathFunctions(unittest.TestCase):

    def test_person(self):
        person = Person(24, 'male', 165, 71, 4)
        print(person.calculate_daily_macros('calories'))
        print(person.calculate_daily_macros('grams'))
        print(person.get_maintanence_calories())

    def test_workout(self):
        # Example usage
        workout1 = Workout("Morning Routine", ["Push-ups", "Sit-ups"])
        workout1.duration = 30
        workout2 = Workout("Evening Routine", ["Jogging", "Stretching"])

        # Adding exercises
        workout1.add_exercise("Pull-ups")

        # Iterating through exercises
        for exercise in workout1:
            print(exercise)

        # Using the class and static methods
        print(Workout.get_workouts_count())
        print(Workout.is_valid_exercise("Squats"))

        # Merging workouts with operator overloading
        merged_workout = workout1 + workout2
        print(merged_workout)

        # Using the Workout class with a context manager
        with Workout("Quick Workout", ["Jumping Jacks", "Plank"]) as workout:
            print(workout)

        # Calling the workout
        workout1()

    def test_trainer(self):
        # Example usage
        trainer = Trainer("John")

        # Creating workouts
        trainer.create_workout("Morning Routine", [Exercise("Push-ups", 10, 3), Exercise("Sit-ups", 20, 3)])
        trainer.create_workout("Evening Routine", [Exercise("Jogging", duration=30), Exercise("Stretching", duration=15)])

        # Listing all workouts
        trainer.list_all_workouts()

        # Creating a person
        person = Person("Alice", 25, "Intermediate")

        # Assigning a workout to a person
        assigned_workout = trainer.assign_workout(person, "Morning Routine")
        if assigned_workout:
            print(f"Assigned Workout: {assigned_workout}")
            
        # Demonstrate context manager
        with Workout("Quick Workout", [Exercise("Jumping Jacks", duration=5)]) as workout:
            print(workout)

        # Calling the workout
        trainer.create_workout("Calisthenics", [Exercise("Pull-ups", 5, 3)])()
