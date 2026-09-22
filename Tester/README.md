# Python Algorithms Tester

A lightweight, zero-dependency Python testing framework designed for competitive programming and computer science assignments. It dynamically runs your Python script, feeds it input files, and checks the output against expected results while analyzing execution time and memory usage.

## Features
- **Data-Driven Testing**: Define tests seamlessly using the **Unified Test Format** (single file) or traditional individual file pairs (`*.in`/`*.out` or `input*.txt`/`output*.txt`).
- **Multi-File Support**: Automatically aggregates all unified test files (e.g. `tests.txt`, `extra_tests.txt`) and individual tests in your target directory into one continuous execution run.
- **Time & Space Complexity**: Measures execution time down to the microsecond and tracks peak memory allocations using Python's built-in `tracemalloc`.
- **Clean Output**: Formatted console output with ANSI colors indicating PASS, FAIL, or ERROR.
- **Detailed Diffing**: If a test fails, it prints out the exact difference between the expected and actual output.
- **Zero Configuration**: Works purely using standard libraries (`sys`, `io`, `time`, `tracemalloc`, `runpy`). 

## Recommended File Structure

Keep your test cases neatly inside a `test_cases/` folder. The tester defaults to scanning this folder.

```text
├── tester.py             # The main testing framework script
├── grades.py             # Your Python assignment script
└── test_cases/           # Directory for your tests
    ├── tests.txt         # Your primary unified tests file
    ├── extra_tests.txt   # (Optional) Additional unified test files
    ├── input1.txt        # (Optional) Traditional separate input file
    └── output1.txt       # (Optional) Traditional separate output file
```

## How to Write Test Cases

Instead of managing dozens of separate input and output files, you can place all your tests into a single **Unified Test File**! You can name the tests and **add comments** anywhere using `#`.

**`test_cases/tests.txt`**
```text
# This is a comment! Tests are defined using '===' blocks.

=== Basic Sort ===
# Testing standard unsorted numbers
--- INPUT ---
5 2 9 1 5 6
--- OUTPUT ---
1 2 5 5 6 9

=== Reverse Sort ===
--- INPUT ---
10 9 8
--- OUTPUT ---
8 9 10
```

*Note: For highly interactive programs that print menus (like `grades.py`), ensure the expected output in your test file exactly matches the full prompt and menu output of your program.*

## How to Run Tests

From your terminal, simply run the `tester.py` script and pass your Python file as an argument. It defaults to scanning the `test_cases/` directory.

```bash
python3 tester.py grades.py
```

### Output Example
```text
Testing Source: grades.py
Tests Source:   test_cases

Test Case                 | Result          | Time (s)   | Peak Memory    
---------------------------------------------------------------------------
tests.txt - Add and View  | PASS            | 0.00017    | 4.4 KB         
extra_tests.txt - Empty   | PASS            | 0.00012    | 4.4 KB         
===========================================================================
Summary: 2/2 tests passed.
```

### Advanced Usage
You can specify a custom file or directory using the `-t` or `--tests` flag:
```bash
python3 tester.py grades.py -t assignment1_tests/
```
