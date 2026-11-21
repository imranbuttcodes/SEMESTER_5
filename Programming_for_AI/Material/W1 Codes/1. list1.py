# A list of mixed types
student_data = ["Awais", 101, 3.85, True, ["Ahmad", "Ali"]]
# print("Before Append: ", student_data)


# # Adding elements
# student_data.append("Semester 6")


# print("After Append", student_data)
# # Accessing by index (same as C++)
# print(student_data[0])  # Output: Awais
# print(student_data[-1]) # Output: Semester 6 (Negative indexing!)

print(student_data[4][0])
import numpy as np
student_data = np.array([
    [1, 20, 3.5],
    [2, 21, 3.2],
    [3, 19, 3.8],
    [4, 22, 3.1],
    [5, 20, 3.9]
])


print(student_data[1:4, 1:3])

