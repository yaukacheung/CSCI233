# Week 4: Functions: Modularity and Scope

## 1. What is a Function?
- A reusable block of code that performs a specific task.
- Prevents code duplication (DRY: Don't Repeat Yourself).

## 2. Defining and Calling Functions
```python
def greet(name):
    return f"Hello, {name}!"

message = greet("Alice")
print(message)
```

## 3. Parameters and Arguments
- **Positional**: `func(1, 2)`
- **Keyword**: `func(a=1, b=2)`
- **Default values**: `def greet(name="User"):`

## 4. Return Values
- Functions can return data using the `return` keyword.
- If no return is specified, it returns `None`.

## 5. Scope
- **Local scope**: Variables defined inside a function.
- **Global scope**: Variables defined outside functions.
