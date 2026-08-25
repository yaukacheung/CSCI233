# Week 11: Object-Oriented Programming (Part 2)

## 1. Inheritance
- Allow a class (Child) to inherit attributes and methods from another class (Parent).
```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Woof!")
```

## 2. Polymorphism
- Objects of different classes can be treated as objects of a common superclass.

## 3. Encapsulation
- Protecting data from outside access using "private" attributes (convention: `_variable` or `__variable`).

## 4. Class Methods and Static Methods
- `@classmethod`: Operates on the class.
- `@staticmethod`: Doesn't need access to the class or instance.

## 5. Composition
- Classes containing objects of other classes (e.g., an `Engine` object inside a `Car` object).
  
