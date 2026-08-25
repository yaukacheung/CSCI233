# Week 7: Strings and File I/O

## 1. Advanced String Formatting
- **f-strings** (Recommended): `f"Hello {name}"`.
- `.format()`: `"Hello {}".format(name)`.

## 2. String Methods
- `strip()`, `split()`, `join()`, `replace()`, `lower()`, `upper()`.

## 3. File Handling (Basics)
- Always use the `with` statement for automatic closing.
- **Reading**:
```python
with open("data.txt", "r") as f:
    content = f.read()
```
- **Writing**:
```python
with open("output.txt", "w") as f:
    f.write("Hello File!")
```

## 4. File Modes
- `r`: Read (default).
- `w`: Write (overwrites).
- `a`: Append (adds to end).
  
