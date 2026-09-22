import unittest
import time
import tracemalloc
import random

# ==========================================
# 1. The Code to be Tested (Example)
# ==========================================
def process_data(arr):
    """
    Example function: Sorts an array. 
    Replace this with the actual function you want to test.
    """
    return sorted(arr)


# ==========================================
# 2. Unit Testing (using built-in 'unittest')
# ==========================================
class TestProcessData(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(process_data([]), [])
        
    def test_already_sorted(self):
        self.assertEqual(process_data([1, 2, 3, 4]), [1, 2, 3, 4])
        
    def test_unsorted_array(self):
        self.assertEqual(process_data([4, 1, 3, 2]), [1, 2, 3, 4])
        
    def test_negative_numbers(self):
        self.assertEqual(process_data([-2, 5, -1, 0]), [-2, -1, 0, 5])


# ==========================================
# 3. Time & Space Complexity Analysis
# ==========================================
def analyze_complexity(func, input_generator, sizes):
    """
    Analyzes time and space complexity empirically by testing 
    the function with increasingly larger inputs.
    
    Args:
        func: The function to test.
        input_generator: A function that takes a size 'n' and returns an input for 'func'.
        sizes: A list of input sizes 'n' to test.
    """
    print(f"{'Input Size (N)':<15} | {'Time (Seconds)':<18} | {'Peak Memory (Bytes)':<20}")
    print("-" * 60)
    
    for n in sizes:
        # Generate input data for the given size
        test_data = input_generator(n)
        
        # Start tracking memory and time
        tracemalloc.start()
        start_time = time.perf_counter()
        
        # Execute the function
        func(test_data)
        
        # Stop tracking time and memory
        end_time = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        time_taken = end_time - start_time
        
        print(f"{n:<15} | {time_taken:<18.6f} | {peak:<20}")

def generate_random_array(n):
    """Helper function to generate a random array of size n."""
    return [random.randint(0, 10000) for _ in range(n)]


# ==========================================
# 4. Execution
# ==========================================
if __name__ == '__main__':
    print("--- Running Time and Space Complexity Analysis ---")
    # Test with different input sizes to observe how time and memory scale
    sizes_to_test = [1000, 10000, 50000, 100000]
    analyze_complexity(process_data, generate_random_array, sizes_to_test)
    
    print("\n--- Running Unit Tests ---")
    # unittest.main() will run all the test methods in TestProcessData
    unittest.main()
