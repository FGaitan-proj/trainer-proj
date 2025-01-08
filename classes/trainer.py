from classes.logging import logging_decorator
from classes.workout_draft import Workout, WorkoutDatabase


class Trainer:
    def __init__(self, name):
        self.name = name
        self.workout_db = WorkoutDatabase()
    
    @logging_decorator
    def create_workout(self, workout_name, exercises):
        workout = Workout(workout_name, exercises)
        self.workout_db.add_workout(workout)
        print(f"Workout '{workout_name}' created and added to the database.")
        return workout

    @logging_decorator
    def assign_workout(self, person, workout_name):
        workout = self.workout_db.get_workout(workout_name)
        if workout:
            print(f"Assigning workout '{workout_name}' to {person}.")
            return workout
        else:
            print(f"Workout '{workout_name}' not found in the database.")
            return None

    def list_all_workouts(self):
        print(f"Workouts in {self.name}'s database:")
        for workout in self.workout_db:
            print(workout)

# Example usage
trainer = Trainer("John")

# Creating workouts
trainer.create_workout("Morning Routine", ["Push-ups", "Sit-ups"])
trainer.create_workout("Evening Routine", ["Jogging", "Stretching"])

# Listing all workouts
trainer.list_all_workouts()

# Creating a person
person = Person("Alice", 25, "Intermediate")

# Assigning a workout to a person
assigned_workout = trainer.assign_workout(person, "Morning Routine")
if assigned_workout:
    print(f"Assigned Workout: {assigned_workout}")
