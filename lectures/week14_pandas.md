# Week 14: Data Science II - Pandas and Matplotlib

## 1. Pandas
- The most popular library for data manipulation.
- **Series**: 1D labeled array.
- **DataFrame**: 2D labeled data structure (like a spreadsheet/SQL table).

## 2. Basic Pandas Operations
```python
import pandas as pd
df = pd.read_csv("data.csv")
print(df.head()) # First 5 rows
print(df.describe()) # Statistical summary
```

## 3. Data Cleaning
- Handling missing values (`dropna()`, `fillna()`).
- Filtering rows and selecting columns.

## 4. Matplotlib / Seaborn
- Visualization tools.
```python
import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()
```

## 5. Why Visualization?
- Identifying trends and patterns.
- Communicating findings clearly.
  +
  
