class WorkoutDatabase:
    def __init__(self):
        self.workouts = []

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



class Workout:
    workouts_count = 0  # Class attribute to keep track of all instances

    def __init__(self, name, exercises):
        self.name = name
        self.exercises = exercises  # List of exercises in the workout
        self._duration = 0  # Protected attribute for workout duration
        Workout.workouts_count += 1

    # String representation
    def __str__(self):
        return f"Workout({self.name}) with {len(self.exercises)} exercises"

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
        return isinstance(exercise, str) and exercise.strip() != ""

    # Add an exercise
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
