import unittest
import pandas as pd


# unittest.main()

# class WorkoutDatabase:
#     """
#     'Exercise', 'Short YouTube Demonstration', 'In-Depth YouTube Explanation', 
#     'Difficulty Level', 'Target Muscle Group ', 'Prime Mover Muscle', 'Secondary Muscle', 'Tertiary Muscle', 
#     'Primary Equipment ', '# Primary Items', 'Secondary Equipment', '# Secondary Items',
#     'Posture', 'Single or Double Arm', 'Continuous or Alternating Arms ', 'Grip', 'Load Position (Ending)', 
#     'Continuous or Alternating Legs ', 'Foot Elevation', 'Combination Exercises', 
#     'Movement Pattern #1', 'Movement Pattern #2', 'Movement Pattern #3', 
#     'Plane Of Motion #1', 'Plane Of Motion #2', 'Plane Of Motion #3', 
#     'Body Region', 'Force Type', 'Mechanics', 'Laterality', 'Primary Exercise Classification'
#     """
#     def __init__(self, dataframe): 
#         self.dataframe = dataframe

#     @classmethod 
#     def from_csv(cls, csv_file): 
#         dataframe = pd.read_csv(csv_file) 
#         return cls(dataframe)

#     def get_unique_values(self, column_name): 
#         return self.dataframe[column_name].unique() 
    
#     def filter_by_attribute(self, attribute, value): 
#         filtered_df = self.dataframe[self.dataframe[attribute] == value] 
#         return filtered_df
    
#     def get_headers(self): 
#         return self.dataframe.columns.tolist()
    


# # Read the CSV file into a DataFrame
# df = WorkoutDatabase.from_csv('exercises.csv')

df = pd.read_csv('exercises.csv') 
print(df.columns.tolist())
print('Target Muscle Group \n\n', df['Target Muscle Group '].unique())
print('Difficulty Level\n\n', df['Difficulty Level'].unique())
print('Body Region\n\n', df['Body Region'].unique())
print('Primary Exercise Classification\n\n', df['Primary Exercise Classification'].unique())
print('Prime Mover Muscle\n\n', df['Prime Mover Muscle'].unique())
print('Secondary Muscle\n\n', df['Secondary Muscle'].unique())
print('Tertiary Muscle\n\n', df['Tertiary Muscle'].unique())
print('Primary Equipment\n\n', df['Primary Equipment '].unique())
print('# Primary Items\n\n', df['# Primary Items'].unique())
print('Secondary Equipment\n\n', df['Secondary Equipment'].unique())
print('# Secondary Items\n\n', df['# Secondary Items'].unique())
print('Posture\n\n', df['Posture'].unique())
print('Single or Double Arm\n\n', df['Single or Double Arm'].unique())
print('Continuous or Alternating Arms\n\n', df['Continuous or Alternating Arms '].unique())
print('Grip\n\n', df['Grip'].unique())
print('Load Position (Ending)\n\n', df['Load Position (Ending)'].unique())
print('Continuous or Alternating Legs\n\n', df['Continuous or Alternating Legs '].unique())
print('Foot Elevation\n\n', df['Foot Elevation'].unique())
print('Combination Exercises\n\n', df['Combination Exercises'].unique())
print('Movement Pattern #1\n\n', df['Movement Pattern #1'].unique())
print('Movement Pattern #2\n\n', df['Movement Pattern #2'].unique())
print('Movement Pattern #3\n\n', df['Movement Pattern #3'].unique())
print('Plane Of Motion #1\n\n', df['Plane Of Motion #1'].unique())
print('Plane Of Motion #2\n\n', df['Plane Of Motion #2'].unique())
print('Plane Of Motion #3\n\n', df['Plane Of Motion #3'].unique())
print('Force Type\n\n', df['Force Type'].unique())
print('Mechanics\n\n', df['Mechanics'].unique())
print('Laterality\n\n', df['Laterality'].unique())
print('Primary Exercise Classification\n\n', df['Primary Exercise Classification'].unique())



# list comprehension
# Generators and Generator Expressions
# decorators
# Context Managers
# itertools
# map, filter, reduce
# metaclass
# dataclasses

"""
Benefits of Using Abstract Classes
Encapsulation: Abstract classes encapsulate common functionality and ensure that certain methods are implemented by all subclasses.

Code Reusability: Promotes code reuse by allowing common methods to be defined in the abstract class and used by multiple subclasses.

Polymorphism: Facilitates polymorphic behavior by providing a common interface for different subclasses.
"""