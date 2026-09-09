import pandas as pd

# Load the dataset
df = pd.read_csv("student_performance.csv")

# Display basic information
print("First 5 records:")
print(df.head())

print("\nDataset Information:")
print(df.info())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Basic statistics
print("\nBasic Statistics:")
print(df.describe())

# Average scores
print("\nAverage Scores:")
print("Average Assignment Score:", df["Assignments_Score"].mean())
print("Average Midterm Score:", df["Midterm_Score"].mean())
print("Average Final Score:", df["Final_Score"].mean())

# Department-wise performance
department_performance = df.groupby("Department")["Final_Score"].mean()
print("\nAverage Final Score by Department:")
print(department_performance.sort_values(ascending=False))

# Top 5 students
top_students = df.nlargest(5, "Final_Score")[
    ["Student_ID", "Department", "Final_Score"]
]

print("\nTop 5 Students:")
print(top_students)

# Study hours vs final score
study_analysis = df.groupby("Study_Hours")["Final_Score"].mean()

print("\nAverage Final Score by Study Hours:")
print(study_analysis)

# Attendance vs final score
attendance_analysis = df.groupby("Attendance")["Final_Score"].mean()

print("\nAttendance vs Final Score:")
print(attendance_analysis)

# Identify students who may need attention
at_risk = df[(df["Attendance"] < 75) | (df["Final_Score"] < 65)]

print("\nStudents Requiring Attention:")
print(at_risk[["Student_ID", "Attendance", "Final_Score"]])
