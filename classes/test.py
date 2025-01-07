from itertools import combinations
from functools import reduce
from dataclasses import dataclass, field
from typing import List

# Metaclass for logging class creation
class LoggingMeta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name}")
        return super().__new__(cls, name, bases, dct)

# Custom Decorator
def logging_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@dataclass
class Exercise:
    name: str
    reps: int = 0
    sets: int = 0
    duration: int = 0  # In minutes

@dataclass
class Person:
    name: str
    age: int
    fitness_level: str

class Workout(metaclass=LoggingMeta):
    workouts_count = 0  # Class attribute to keep track of all instances

    def __init__(self, name: str, exercises: List[Exercise]):
        self.name = name
        self.exercises = exercises  # List of exercises in the workout
        self._duration = 0  # Protected attribute for workout duration
        Workout.workouts_count += 1

    # String representation
    def __str__(self):
        exercise_names = ", ".join(exercise.name for exercise in self.exercises)
        return f"Workout({self.name}) with exercises: {exercise_names}"

    # Official representation
    def __repr__(self):
        return f"Workout('{self.name}', {self.exercises})"

    # Destructor
    def __del__(self):
        Workout.workouts_count -= 1
        print(f"Deleted Workout instance: {self.name}")

    # Property for duration with getter, setter, and deleter
    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        self._duration = value

    @duration.deleter
    def duration(self):
        del self._duration

    # Class method to get the count of Workout instances
    @classmethod
    def get_workouts_count(cls):
        return cls.workouts_count

    # Static method to check if an exercise is valid
    @staticmethod
    def is_valid_exercise(exercise):
        return isinstance(exercise, Exercise) and exercise.name.strip() != ""

    @logging_decorator
    def add_exercise(self, exercise):
        if self.is_valid_exercise(exercise):
            self.exercises.append(exercise)
        else:
            raise ValueError("Invalid exercise")

    # Iterable methods
    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index < len(self.exercises):
            result = self.exercises[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration

    # Operator overloading for addition
    def __add__(self, other):
        if isinstance(other, Workout):
            combined_exercises = [*self.exercises, *other.exercises]
            return Workout(f"{self.name} & {other.name}", combined_exercises)
        return NotImplemented

    # Len, Getitem, Setitem, Delitem
    def __len__(self):
        return len(self.exercises)

    def __getitem__(self, index):
        return self.exercises[index]

    def __setitem__(self, index, value):
        if self.is_valid_exercise(value):
            self.exercises[index] = value
        else:
            raise ValueError("Invalid exercise")

    def __delitem__(self, index):
        del self.exercises[index]

    # Call method
    def __call__(self):
        print(f"Let's start the workout: {self.name}")

    # Context manager methods
    def __enter__(self):
        print(f"Starting workout: {self.name}")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Finished workout: {self.name}")

class WorkoutDatabase:
    def __init__(self):
        self.workouts = []

    @logging_decorator
    def add_workout(self, workout):
        self.workouts.append(workout)

    def get_workout(self, name):
        for workout in self.workouts:
            if workout.name == name:
                return workout
        return None

    def __iter__(self):
        return iter(self.workouts)

    def __str__(self):
        return f"WorkoutDatabase with {len(self.workouts)} workouts"

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
