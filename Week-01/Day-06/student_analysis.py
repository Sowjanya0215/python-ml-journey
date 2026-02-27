#csv file---

name,gender,math_marks,science_marks,english_marks,attendance
Rahul,Male,85,78,88,92
Sneha,Female,90,91,87,95
Arjun,Male,76,72,70,85
Priya,Female,88,84,90,93
Kiran,Male,65,60,58,80
Anjali,Female,92,89,94,97
Vikram,Male,55,62,59,75
Divya,Female,78,85,80,88
Rohit,Male,83,79,85,90
Meena,Female,70,68,72,82
Suresh,Male,,74,69,86
Lavanya,Female,89,,91,94
Karthik,Male,95,93,96,98
Pooja,Female,60,58,,78
Rahul,Male,85,78,88,92

#code---

import pandas as pd
import numpy as np

# -------------------------------
# 1. Load Dataset
# -------------------------------
df = pd.read_csv("students.csv")

print("First 5 Rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

# -------------------------------
# 2. Data Cleaning
# -------------------------------

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Fill missing numeric values with mean
numeric_columns = ["math_marks", "science_marks", "english_marks", "attendance"]

for col in numeric_columns:
    if col in df.columns:
        df[col].fillna(df[col].mean(), inplace=True)

# Fill missing categorical values with mode
categorical_columns = ["name", "gender"]

for col in categorical_columns:
    if col in df.columns:
        df[col].fillna(df[col].mode()[0], inplace=True)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# -------------------------------
# 3. Feature Engineering
# -------------------------------

# Calculate total marks
df["total_marks"] = (
    df["math_marks"] +
    df["science_marks"] +
    df["english_marks"]
)

# Calculate average marks
df["average"] = df["total_marks"] / 3

# Assign performance grade
def assign_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "D"

df["performance_grade"] = df["average"].apply(assign_grade)

# -------------------------------
# 4. Data Analysis
# -------------------------------

print("\nTop 5 Students:")
top_students = df.sort_values(by="average", ascending=False).head(5)
print(top_students[["name", "average"]])

print("\nSubject-wise Average:")
print(df[["math_marks", "science_marks", "english_marks"]].mean())

print("\nGender-wise Average Performance:")
print(df.groupby("gender")["average"].mean())

print("\nAttendance vs Performance Grade:")
print(df.groupby("performance_grade")["attendance"].mean())

# -------------------------------
# 5. Additional Insights
# -------------------------------

print("\nHighest Scorer in Each Subject:")
print("Math:", df.loc[df["math_marks"].idxmax(), "name"])
print("Science:", df.loc[df["science_marks"].idxmax(), "name"])
print("English:", df.loc[df["english_marks"].idxmax(), "name"])

print("\nCorrelation Between Subjects:")
print(df[["math_marks", "science_marks", "english_marks"]].corr())

# -------------------------------
# 6. Save Cleaned Data
# -------------------------------

df.to_csv("updated_students.csv", index=False)

print("\nCleaned dataset saved as updated_students.csv")
