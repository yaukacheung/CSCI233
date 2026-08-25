# Week 5: Sequential Data - Lists and Tuples

## 1. Lists
- Ordered, mutable (changeable) collections.
```python
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits[0]) # "apple"
```

## 2. Common List Methods
- `append()`, `remove()`, `pop()`, `sort()`, `len()`.

## 3. Slicing
- Extracting parts of a list.
```python
nums = [0, 1, 2, 3, 4, 5]
print(nums[1:4]) # [1, 2, 3]
```

## 4. Tuples
- Ordered, **immutable** (unchangeable) collections.
- Defined with parentheses `()`.
```python
coordinates = (10, 20)
# coordinates[0] = 15 # THIS WILL ERROR
```

## 5. List Comprehensions
- Concise way to create lists.
```python
squares = [x**2 for x in range(10)]
```
