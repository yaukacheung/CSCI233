
import numpy as np

# ==========================
# 1. BASIC ARRAYS
# ==========================

# Create two 3x3 arrays
array1 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

array2 = np.array([
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
])

print("===== MATRIX OPERATIONS =====")

print("\nFirst Array:")
print(array1)

print("\nSecond Array:")
print(array2)

# Add the arrays
print("\nSum of Arrays:")
print(array1 + array2)

# Multiply the arrays element by element
print("\nProduct of Arrays (Element-wise):")
print(array1 * array2)

# Matrix multiplication
print("\nMatrix Multiplication:")
print(np.dot(array1, array2))


# ==========================
# 2. STATISTICS
# ==========================

print("\n===== STATISTICS =====")

# Generate 100 random numbers
random_numbers = np.random.rand(100)

print("\nRandom Numbers:")
print(random_numbers)

# Calculate mean
mean = np.mean(random_numbers)

# Calculate standard deviation
std_dev = np.std(random_numbers)

print("\nMean:", mean)
print("Standard Deviation:", std_dev)


# ==========================
# 3. CHALLENGE: LINEAR EQUATIONS
# ==========================

print("\n===== SOLVING LINEAR EQUATIONS =====")

# Solve the following system:
# 2x + y = 8
# x + 3y = 9

coefficients = np.array([
    [2, 1],
    [1, 3]
])

constants = np.array([8, 9])

# Solve using NumPy
solution = np.linalg.solve(coefficients, constants)

print("\nSolution:")
print("x =", solution[0])
print("y =", solution[1])
