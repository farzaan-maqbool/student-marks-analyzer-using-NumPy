import numpy as np
marks=np.array([
    [85,90,78,88,92],
    [70,75,80,72,78],
    [95,92,94,96,98],
    [60,65,58,70,62],
    [88,84,90,86,89]
])
print(marks)
print("Shape: ",marks.shape)
print("Dimensions: ",marks.ndim)

student_average=np.mean(marks,axis=1)
print("Student averages: ",student_average)

subject_average=np.mean(marks,axis=0)
print("Subject averages: ",subject_average)
highest=np.max(marks)
lowest=np.min(marks)
print("Highest marks : ",highest)
print("Lowest marks : ",lowest)

top_student_index=np.argmax(student_average)
print("Top student Index : ",top_student_index)
print("Top student average: ",student_average[top_student_index])

students=np.array([
    "Student 1",
    "Student 2",
    "Student 3",
    "Student 4",
    "Student 5"
])
print("Top Student : ",students[top_student_index])

passed=np.all(marks>=40,axis=1)
print("Pass status : ",passed)
print("Passed students ",students[passed])
print("Failed students ",students[~passed])