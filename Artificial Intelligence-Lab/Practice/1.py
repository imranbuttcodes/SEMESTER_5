# # numbers = {10, 20}

# # numbers.update([30, 40, 50])

# # print(numbers)


# # try:
# #     numbers.remove(22)
# # except KeyError:
# #     print("22 is not present in the set")

# # #numbers.discard(20)

# # print(numbers)

# # print(numbers.pop())


# student_ids = [1, 2, 3, 4, 5, 1]
# d = dict.fromkeys(student_ids)
# print(d)
# print(list(d))
# #d[1] = "Bro"
# print(set(student_ids))

# d = {

# }



# student = {
#     "name": "Imran",
#     "age": 20,
#     "department": "CS"
# }
# print(type(student.keys()))

# print(student.keys())


text = "banana"
frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print(frequency)
