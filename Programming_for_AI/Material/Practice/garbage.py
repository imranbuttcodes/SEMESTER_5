# # # # # def calculate(*args, **kwargs):
# # # # #     print(args)
# # # # #     print(kwargs)


# # # # # lst = [1,2,3,4,5,6]
# # # # # data = {
# # # # #     "name": "Imran",
# # # # #     "age": 21,
# # # # #     "gpa": 3.66
# # # # # }

# # # # # data2 = {
# # # # #     "AI": "Imran12",
# # # # #     "BRO": 2112,
# # # # #     "YOAH": 3.6612
# # # # # }

# # # # # result = {**data, **data2}

# # # # # print(result)
# # # # # # numbers = [10, 20, 30, 40, 50]

# # # # # # *a, b, c = numbers

# # # # # # print(a)
# # # # # # print(b)
# # # # # # print(c)
# # # # # #calculate(*lst, **dct)



# # # # # Decorators

# # # # import time
# # # # def timer_decorator(func):

# # # #     def wrapper(*args, **kwargs):
# # # #         start = time.perf_counter()

# # # #         result = func(*args, **kwargs)

# # # #         print(f"Execution time: {time.perf_counter() - start:.4f}s")

# # # #         return result

# # # #     return wrapper

# # # # @timer_decorator
# # # # def slow_math(a, b):
# # # #     print("called")
# # # #     time.sleep(1)
# # # #     return "Done :" + str(a - b)

# # # # # slow_math = timer_decorator(slow_math)

# # # # slow_math(1, 2)



# # # def fibonacci_gen(limit):
# # #     a, b = 0, 1
# # #     count = 0
# # #     print("Here I'm ")
# # #     while count < limit:
# # #         yield a
# # #         a, b = b, a + b
# # #         count += 1

# # # # This does NOT store 1 million numbers in RAM

# # # for num in fibonacci_gen(1000000):
# # #     if num > 100: break
# # #     print(num)

# # #     #    f(n) = f(n-1) + f(n-2)



# # import random

# # def image_batch_generator(batch_size):
# #     while True:
# #         # Simulate loading images from disk
# #         batch = [f"Image_Data_{random.randint(1, 100)}" for _ in range(batch_size)]
# #         yield batch  # Yields a batch, then waits for the next request

# # # AI Training Loop
# # loader = image_batch_generator(32)
# # for i in range(3):
# #     print(f"Training on: {next(loader)}")
# #     print()

# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Fri Mar 13 09:26:35 2026

# @author: awais
# """

# # Generator

# def ucp_range(size):
#     count = 0
#     while count < size:
#         print("generating: ", str(count))
#         yield count
#         count += 1
        

# for i in ucp_range(100):
#     print(i)
# print(ucp_range(10))
# print(range(100))

# List comprehension
# a = [x * 2 for x in range(5)]

# # Generator expression
# b = (x * 2 for x in range(5))

# for _ in a:
#     print(_)

# print()
# for _ in b:

#     print(_)

x = "global"

def outer():
    x = "enclosing"
    def inner():
        global x
        x = "local" 
        print("1: ", x) # Searches L -> E -> G -> B
        if True:
            x = "inside if"
            print("2: ", x)
        print("3: ", x)
    inner()
    print("4: ", x)

outer()
print("5: ", x)