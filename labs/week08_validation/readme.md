# Lab 8: Robust Input Validator

## Objectives
1. Prevent crashes using `try/except`.
2. Validate user data.
3. Use custom error messages.

## Tasks
1. **Safe Division**:
    - Create `safe_calc.py`.
    - Ask for two numbers and divide them. Use `try/except` to catch `ValueError` and `ZeroDivisionError`.
2. **File Validator**:
    - Ask the user for a filename.
    - Try to open it. Catch `FileNotFoundError`.

## Challenge
- Create a function that asks for an integer within a specific range (e.g., 1-10) and keeps asking until a valid input is given.
