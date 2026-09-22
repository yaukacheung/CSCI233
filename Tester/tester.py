#!/usr/bin/env python3
import sys
import io
import time
import tracemalloc
import runpy
import argparse
import os
import glob

# ANSI Color Codes for Terminal Output
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
RESET = '\033[0m'

def run_test_case(source_file, input_data):
    """Runs a Python script and captures its stdout, time taken, and peak memory."""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    
    sys.stdin = io.StringIO(input_data)
    captured_stdout = io.StringIO()
    sys.stdout = captured_stdout
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    error_msg = None
    try:
        # Execute the target Python script in the current process space
        runpy.run_path(source_file, run_name="__main__")
    except Exception as e:
        error_msg = str(e)
        
    end_time = time.perf_counter()
    _, peak_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    output_data = captured_stdout.getvalue()
    
    sys.stdin = old_stdin
    sys.stdout = old_stdout
    
    time_taken = end_time - start_time
    return output_data, time_taken, peak_memory, error_msg

def parse_unified_tests_file(filepath):
    """Parses a unified test cases file into a list of test dictionaries."""
    tests = []
    current_test = None
    state = None
    
    with open(filepath, 'r') as f:
        for line in f:
            # Ignore lines that start with '#' (comments)
            if line.strip().startswith('#'):
                continue
                
            if line.startswith('==='):
                name = line.strip('=\n ').strip()
                if not name:
                    name = f"Test {len(tests) + 1}"
                current_test = {'name': name, 'input': [], 'output': []}
                tests.append(current_test)
                state = None
            elif line.startswith('--- INPUT ---'):
                state = 'INPUT'
            elif line.startswith('--- OUTPUT ---'):
                state = 'OUTPUT'
            else:
                if state == 'INPUT' and current_test is not None:
                    current_test['input'].append(line)
                elif state == 'OUTPUT' and current_test is not None:
                    current_test['output'].append(line)
                    
    for t in tests:
        t['input'] = "".join(t['input'])
        t['output'] = "".join(t['output'])
        
    return tests

def find_test_files(tests_dir):
    """Finds input and expected output file pairs in a directory."""
    input_files = []
    
    # Check for .in / .out competitive programming format
    in_files = glob.glob(os.path.join(tests_dir, "*.in"))
    if in_files:
        for in_f in in_files:
            out_f = in_f[:-3] + ".out"
            input_files.append((in_f, out_f))
    else:
        # Check for input*.txt / output*.txt format
        txt_files = glob.glob(os.path.join(tests_dir, "input*.txt"))
        for txt_f in txt_files:
            base = os.path.basename(txt_f)
            out_name = base.replace("input", "output")
            out_f = os.path.join(tests_dir, out_name)
            input_files.append((txt_f, out_f))
            
    return sorted(input_files)

def evaluate_and_print_result(name, actual, expected, time_taken, peak_memory, error_msg):
    """Compares the actual vs expected output and prints the table row."""
    mem_kb = f"{peak_memory / 1024:.1f} KB"
    
    if error_msg:
        result_str = f"{RED}ERROR{RESET}"
        passed = False
    else:
        passed = (actual.strip() == expected.strip())
        result_str = f"{GREEN}PASS{RESET}" if passed else f"{RED}FAIL{RESET}"

    # Trim the name if it's too long
    display_name = name[:22] + "..." if len(name) > 25 else name
    print(f"{display_name:<25} | {result_str:<24} | {time_taken:<10.5f} | {mem_kb:<15}")
    
    if not passed:
        if error_msg:
            print(f"   {RED}[Exception]{RESET}: {error_msg}")
        else:
            print(f"   {CYAN}[Expected]{RESET}: {expected.strip()}")
            print(f"   {RED}[Actual]  {RESET}: {actual.strip()}")
        print("-" * 75)
        
    return passed

def run_all_tests(source_file, tests_path):
    if not os.path.exists(source_file):
        print(f"{RED}Error: Source file '{source_file}' not found.{RESET}")
        return
    if not os.path.exists(tests_path):
        print(f"{RED}Error: Tests path '{tests_path}' not found.{RESET}")
        return

    print(f"{'Test Case':<25} | {'Result':<15} | {'Time (s)':<10} | {'Peak Memory':<15}")
    print("-" * 75)

    passed_count = 0
    total_count = 0
    tests_to_run = [] # List of tuples: (name, input_data, expected_data)

    if os.path.isfile(tests_path):
        # Single unified test file provided
        unified_tests = parse_unified_tests_file(tests_path)
        for t in unified_tests:
            tests_to_run.append((t['name'], t['input'], t['output']))

    elif os.path.isdir(tests_path):
        # 1. Discover all unified test files (e.g. tests.txt, grade_tests.txt)
        unified_files = glob.glob(os.path.join(tests_path, "*test*.txt"))
        
        # Ensure tests.txt is included even if it misses the glob somehow
        default_tests = os.path.join(tests_path, "tests.txt")
        if default_tests not in unified_files and os.path.exists(default_tests):
            unified_files.append(default_tests)

        unified_files = sorted(list(set(unified_files)))

        for uf in unified_files:
            file_base = os.path.basename(uf)
            unified_tests = parse_unified_tests_file(uf)
            for t in unified_tests:
                # Prefix the test name with the file name to avoid ambiguity
                tests_to_run.append((f"{file_base} - {t['name']}", t['input'], t['output']))

        # 2. Discover directory of separated test files (input1.txt / output1.txt)
        test_pairs = find_test_files(tests_path)
        for in_file, out_file in test_pairs:
            base_name = os.path.basename(in_file)
            if not os.path.exists(out_file):
                print(f"{base_name:<25} | {YELLOW + 'SKIPPED' + RESET:<24} | Missing output: {os.path.basename(out_file)}")
                continue
                
            with open(in_file, 'r') as f: input_data = f.read()
            with open(out_file, 'r') as f: expected_data = f.read()
            tests_to_run.append((base_name, input_data, expected_data))

    if not tests_to_run:
        print(f"{YELLOW}No test cases found in '{tests_path}'.{RESET}")
        return

    # Execute all collected tests
    for name, input_data, expected_data in tests_to_run:
        total_count += 1
        actual_data, time_taken, peak_memory, error_msg = run_test_case(source_file, input_data)
        passed = evaluate_and_print_result(name, actual_data, expected_data, time_taken, peak_memory, error_msg)
        if passed: 
            passed_count += 1

    print("=" * 75)
    summary_color = GREEN if passed_count == total_count and total_count > 0 else RED
    print(f"{summary_color}Summary: {passed_count}/{total_count} tests passed.{RESET}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test a Python script against input and expected output files.")
    parser.add_argument("source", help="The Python (.py) file to test.")
    parser.add_argument("--tests", "-t", default="test_cases", help="Path to a unified tests.txt file OR a directory containing test files (default: 'test_cases').")
    
    args = parser.parse_args()
    
    print(f"{CYAN}Testing Source:{RESET} {args.source}")
    print(f"{CYAN}Tests Source:  {RESET} {args.tests}\n")
    run_all_tests(args.source, args.tests)
