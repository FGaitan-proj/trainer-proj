from dataclasses import dataclass
import pandas as pd
from classes.logging import logging_decorator
from enum import Enum

class ExerciseType(Enum):
    FULL_BODY = "Full body"
    UPPER_BODY = "Upper body"
    LOWER_BODY = "Lower body"

    PUSH = "Push"
    PULL = "Pull"
    LEGS = "legs"
    
    HIIT = "HIIT"
    CARDIO = "Cardio"
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



# this class will provide a single workout routine
# TODO get the routine to generate a list of exercises
# TODO filter the exercises by the difficulty level
# TODO determine which exercise types will have compound and isolation
# TODO get the duration to impact the reps and sets
# TODO have the list of routines list[Workout] have an attribute: targeted muscle groups
class Workout:
    def __init__(self, duration: int, name: str ='', 
                 routine: list[ExerciseType] = [
                     ExerciseType.WARM_UP, 
                     ExerciseType.FULL_BODY, 
                     ExerciseType.COOLDOWN
                 ]):
        self._name = name
        self._duration = duration  # Protected attribute for workout duration
        self.routine = routine  # List of exercises in the workout

    # String representation
    def __str__(self): 
        return f"Workout({self._name}): {len(self.routine)} exercises"

    # Official representation
    def __repr__(self):
        return f"Workout('{self._name}', {self.routine})"
    
    @property
    def duration(self) -> int:
        return self._duration
    
    def _generate_workout(self, etype: ExerciseType) -> Exercise:
        if etype in [ExerciseType.FULL_BODY, ExerciseType.UPPER_BODY, ExerciseType.LOWER_BODY]:
            # ['Body Region']
            # ['Midsection' 'Lower Body' 'Upper Body' 'Full Body' 'Unsorted*']
            pass
        elif etype == [ExerciseType.PUSH, ExerciseType.PULL, ExerciseType.LEGS]:
            # Movement Pattern #1
            push = [
                'Horizontal Push', 'Vertical Push', 'Shoulder Flexion', 
                'Shoulder Abduction', 'Elbow Extension', 'Shoulder Internal Rotation', 
                'Shoulder Scapular Plane Elevation'
            ]

            pull = [
                'Horizontal Pull', 'Vertical Pull', 'Shoulder External Rotation', 
                'Elbow Flexion', 'Scapular Elevation', 'Loaded Carry'
            ]

            leg = [
                'Hip Extension', 'Hip Flexion', 'Hip External Rotation', 
                'Hip Adduction', 'Hip Hinge', 'Hip Abduction', 
                'Knee Dominant', 'Ankle Plantar Flexion', 'Ankle Dorsiflexion'
            ]

            others = [
                'Anti-Extension', 'Anti-Rotational', 'Rotational', 'Spinal Flexion', 
                'Lateral Flexion', 'Anti-Lateral Flexion', 'Isometric Hold', 
                'Spinal Extension', 'Wrist Flexion', 'Wrist Extension', 
                'Anti-Flexion'
            ]

            pass
        else:
            # ['Primary Exercise Classification']
            # [ 'Bodybuilding' 'Grinds' 'Powerlifting' 
            #  'Olympic Weightlifting' '*Unsorted' 'Unsorted*' 'Olympic Weightlifting ']

            """
                HIIT = "HIIT"               "Plyometric", "Ballistics"
                CARDIO = "Cardio"           "Animal Flow", "Calisthenics"
                WARM_UP = "warm up"         "Mobility"
                COOLDOWN = "cooldown"       "Mobility"
                STRETCHING = "stretching"   "Mobility", "Postural", "Balance"
                YOGA = "yoga"               "Mobility", "Postural", "Balance"
                PILATES = "pilates"         "Mobility", "Postural", "Balance", "Calisthenics"
            """
            pass
        return


    def get_workout(self) -> list[Exercise]:
        workouts = []
        for exercise in self.routine:
            self._generate_workout(exercise)
            workouts.append
        return workouts
    

    # @duration.setter
    # def duration(self, value):
    #     self._duration = value

    # # function that will edit the reps and sets for a specific exercise in 
    # def edit_exercise(self, exercise, reps, sets):
    #     exercise.reps = reps
    #     exercise.sets = sets
