# Week 8: Exception Handling

## 1. Why Handle Errors?
- Prevents the program from crashing.
- Provides user-friendly feedback.

## 2. Try/Except Blocks
```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input! Please enter a number.")
```

## 3. Else and Finally
- `else`: Runs if NO exceptions occurred.
- `finally`: Runs NO MATTER WHAT (useful for cleanup).

## 4. Raising Exceptions
- Use `raise` to manually trigger an error.
```python
if age < 0:
    raise ValueError("Age cannot be negative")
```
  
