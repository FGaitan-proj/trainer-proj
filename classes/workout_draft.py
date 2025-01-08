from dataclasses import dataclass
import pandas as pd
from classes.logging import logging_decorator
from enum import Enum

class ExerciseType(Enum):
    HIIT = "HIIT"
    PUSH = "Push"
    PULL = "Pull"
    CARDIO = "Cardio"
    FULL_BODY = "Full body"
    LEGS = "legs"
    WARM_UP = "warm up"
    COOLDOWN = "cooldown"
    STRETCHING = "stretching"
    YOGA = "yoga"
    PILATES = "pilates"



@dataclass
class Exercise:
    name: str
    reps: int = 0
    sets: int = 0
    duration: int = 0  # In minutes
    details: list[str] = []




class Workout:
    workouts_count = 0  # Class attribute to keep track of all instances

    def __init__(self, duration, name='', routine: list[ExerciseType] = [ExerciseType.WARM_UP, ExerciseType.FULL_BODY, ExerciseType.COOLDOWN]):
        self._name = name
        self._duration = duration  # Protected attribute for workout duration
        self.routine = routine  # List of exercises in the workout

    # String representation
    def __str__(self):
        return f"Workout({self._name}): {len(self.exercises)} exercises"

    # Official representation
    def __repr__(self):
        return f"Workout('{self._name}', {self.exercises})"



    def load_workouts(self, dataframe): 
        workouts = [] 
        for index, row in dataframe.iterrows():
            workout = Exercise(
                name=row['name'], 
                reps=row.get('reps', 0), 
                sets=row.get('sets', 0), 
                duration=row.get('duration', 0)) 
            workouts.append(workout) 
        return workouts
    
    # # function that given duration and routine, will return a recommended sets and reps
    # def get_recommended_sets_reps(self, duration, routine):
    #     if duration < 30:
    #         return 1, 10
    #     elif duration < 60:
    #         return 2, 15
    #     else:
    #         return 3, 20
    
    # def _load_workouts(self, dataframe, duration): 
    #     workouts = [] 
    #     for index, row in dataframe.iterrows():
    #         workout = Exercise(
    #             name=row['name'], 
    #             reps=row.get('reps', 0), 
    #             sets=row.get('sets', 0), 
    #             duration=row.get('duration', 0)) 
    #         workouts.append(workout) 
    #     return workouts

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
        return isinstance(exercise, str) and exercise.strip() != ""

    # Add an exercise
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
            return Workout(f"{self.name} & {other.name}", self.exercises + other.exercises)
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
