# Student Getting Started Guide: CSCI233 Python Programming

Welcome to the course! This guide will help you set up your environment and understand how to complete and verify your work.

## 1. Environment Setup
### Install Python
- Download and install Python 3.10 or higher from [python.org](https://www.python.org/).
- On macOS/Linux, you might need to use `python3` and `pip3` instead of `python` and `pip`.

### Install VS Code (Recommended)
- Download from [code.visualstudio.com](https://code.visualstudio.com/).
- Install the **Python** extension by Microsoft.

### Install Required Tools
Open your terminal and run:
```bash
pip install pytest requests pandas numpy matplotlib
```

## 2. Course Structure
- **lectures/**: Weekly theory notes. Read these before the lab.
- **labs/**: Practical exercises. You should complete these every week.
- **assignments/**: Large projects due at key milestones.
- **quizzes/**: Weekly checks for understanding.

## 3. Verifying Your Work
We use an automated test runner to ensure your code produces the correct output.

1. Navigate to the root of your project.
2. Run the tests:
   ```bash
   python tests/run_tests.py
   ```
3. Read the output. If a test fails, it will tell you what was missing from your output.

## 4. Submission Guidelines
- Ensure your filenames match the instructions exactly (e.g., `calculator.py` vs `my_calc.py`).
- Do not remove the `tests/` directory; it is needed for verification.
- Always check that your code runs without errors before submitting.

Good luck!
