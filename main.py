from classes.person import Person

person = Person(24, 'male', 165, 71, 4)

print(person.calculate_daily_macros('calories'))
print(person.calculate_daily_macros('grams'))
print(person.get_maintanence_calories())


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