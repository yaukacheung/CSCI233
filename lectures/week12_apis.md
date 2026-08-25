# Week 12: Working with APIs and JSON

## 1. What is an API?
- Application Programming Interface.
- A way for different software systems to communicate.

## 2. REST APIs
- Use HTTP requests (`GET`, `POST`, `PUT`, `DELETE`).

## 3. JSON (JavaScript Object Notation)
- The standard format for data exchange on the web.
- Looks very similar to Python dictionaries.
```json
{
  "status": "success",
  "data": [1, 2, 3]
}
```

## 4. Parsing JSON in Python
```python
import json
data = '{"name": "Alice"}'
user = json.loads(data) # String to Dict
```

## 5. Authentication
- Most APIs require an API Key or Token.
  +
  
