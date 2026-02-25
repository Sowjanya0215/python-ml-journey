import numpy as np

# Marks of 3 students in 4 subjects
# Rows = Students
# Columns = Subjects
marks = np.array([
    [85, 78, 92, 88],
    [75, 80, 79, 83],
    [90, 92, 88, 95]
])

print("Student Marks:\n", marks)

# Total marks of each student
total = np.sum(marks, axis=1)
print("\nTotal Marks of Each Student:", total)

# Average marks of each student
average = np.mean(marks, axis=1)
print("\nAverage Marks of Each Student:", average)

# Highest mark in each subject
highest = np.max(marks, axis=0)
print("\nHighest Marks in Each Subject:", highest)

# Lowest mark in each subject
lowest = np.min(marks, axis=0)
print("\nLowest Marks in Each Subject:", lowest)

# Overall class average
class_avg = np.mean(marks)
print("\nOverall Class Average:", class_avg)

# Topper (student index + 1)
topper = np.argmax(total) + 1
print("\nTopper is Student:", topper)
