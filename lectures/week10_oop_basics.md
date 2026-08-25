# Week 10: Object-Oriented Programming (Part 1)

## 1. What is OOP?
- A programming paradigm based on "objects" that contain data (attributes) and code (methods).

## 2. Classes vs. Objects
- **Class**: The blueprint (e.g., `Car`).
- **Object/Instance**: The actual thing (e.g., my Toyota).

## 3. The `__init__` Method
- The constructor. Initializes the object's attributes.
```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
```

## 4. Methods
- Functions defined inside a class that act on the object.
```python
class Dog:
    # ...
    def bark(self):
        print(f"{self.name} says Woof!")
```

## 5. `self`
- Represents the instance of the class. Essential for accessing attributes and methods.
