# Week 6: Mapping Data - Dictionaries and Sets

## 1. Dictionaries
- Unordered, mutable collections of key-value pairs.
- Keys must be unique and immutable (strings, numbers).
```python
user = {
    "name": "Alice",
    "age": 25,
    "email": "alice@example.com"
}
print(user["name"]) # "Alice"
```

## 2. Common Dictionary Operations
- Accessing: `dict[key]` or `dict.get(key)`.
- Adding/Updating: `dict[key] = value`.
- Removing: `pop()`, `del`.
- Iterating: `.keys()`, `.values()`, `.items()`.

## 3. Sets
- Unordered collections of **unique** elements.
- Useful for removing duplicates and mathematical operations (union, intersection).
```python
numbers = {1, 2, 2, 3}
print(numbers) # {1, 2, 3}
```

## 4. Set Operations
- `add()`, `remove()`.
- `|` (union), `&` (intersection), `-` (difference).
  
