# pip install pandas matplotlib

import pandas as pd
import matplotlib.pyplot as plt

# ==========================
# 1. LOAD TITANIC DATASET
# ==========================

# Download and load the Titanic CSV dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"

df = pd.read_csv(url)

print("===== TITANIC DATASET =====")

# Display first five rows
print("\nFirst Five Rows:")
print(df.head())

# Display dataset information
print("\nDataset Information:")
print(df.info())


# ==========================
# 2. SURVIVAL ANALYSIS
# ==========================

print("\n===== SURVIVAL ANALYSIS =====")

# Calculate overall survival rate
survival_rate = df["survived"].mean() * 100

print(f"\nOverall Survival Rate: {survival_rate:.2f}%")

# Count survivors and non-survivors
survivors = df["survived"].value_counts()

print("\nPassenger Survival Counts:")
print("Survived:", survivors.get(1, 0))
print("Did Not Survive:", survivors.get(0, 0))


# ==========================
# 3. SURVIVAL BY GENDER
# ==========================

print("\n===== SURVIVAL BY GENDER =====")

gender_survival = df.groupby("sex")["survived"].mean() * 100

print("\nSurvival Rates by Gender:")
print(gender_survival)


# ==========================
# 4. AVERAGE PASSENGER AGE
# ==========================

print("\n===== AVERAGE AGE =====")

average_age = df["age"].mean()

print(f"\nAverage Passenger Age: {average_age:.2f} years")


# ==========================
# 5. BAR CHART
# ==========================

print("\nCreating Survival Bar Chart...")

survival_counts = df["survived"].value_counts().sort_index()

plt.figure(figsize=(8, 5))

plt.bar(
    ["Did Not Survive", "Survived"],
    survival_counts.values,
    color=["red", "green"]
)

plt.title("Titanic Passenger Survival Count")
plt.xlabel("Survival Status")
plt.ylabel("Number of Passengers")

plt.tight_layout()
plt.show()


# ==========================
# 6. CHALLENGE: AGE HISTOGRAM
# ==========================

print("\nCreating Age Histogram...")

plt.figure(figsize=(8, 5))

plt.hist(
    df["age"].dropna(),
    bins=20,
    color="skyblue",
    edgecolor="black"
)

plt.title("Distribution of Titanic Passenger Ages")
plt.xlabel("Age")
plt.ylabel("Number of Passengers")

plt.tight_layout()
plt.show()

print("\n===== ANALYSIS COMPLETE =====")
