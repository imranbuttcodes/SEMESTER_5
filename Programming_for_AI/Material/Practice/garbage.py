# # # # # # # # # # # # # # # # # # def calculate(*args, **kwargs):
# # # # # # # # # # # # # # # # # #     print(args)
# # # # # # # # # # # # # # # # # #     print(kwargs)


# # # # # # # # # # # # # # # # # # lst = [1,2,3,4,5,6]
# # # # # # # # # # # # # # # # # # data = {
# # # # # # # # # # # # # # # # # #     "name": "Imran",
# # # # # # # # # # # # # # # # # #     "age": 21,
# # # # # # # # # # # # # # # # # #     "gpa": 3.66
# # # # # # # # # # # # # # # # # # }

# # # # # # # # # # # # # # # # # # data2 = {
# # # # # # # # # # # # # # # # # #     "AI": "Imran12",
# # # # # # # # # # # # # # # # # #     "BRO": 2112,
# # # # # # # # # # # # # # # # # #     "YOAH": 3.6612
# # # # # # # # # # # # # # # # # # }

# # # # # # # # # # # # # # # # # # result = {**data, **data2}

# # # # # # # # # # # # # # # # # # print(result)
# # # # # # # # # # # # # # # # # # # numbers = [10, 20, 30, 40, 50]

# # # # # # # # # # # # # # # # # # # *a, b, c = numbers

# # # # # # # # # # # # # # # # # # # print(a)
# # # # # # # # # # # # # # # # # # # print(b)
# # # # # # # # # # # # # # # # # # # print(c)
# # # # # # # # # # # # # # # # # # #calculate(*lst, **dct)



# # # # # # # # # # # # # # # # # # Decorators

# # # # # # # # # # # # # # # # # import time
# # # # # # # # # # # # # # # # # def timer_decorator(func):

# # # # # # # # # # # # # # # # #     def wrapper(*args, **kwargs):
# # # # # # # # # # # # # # # # #         start = time.perf_counter()

# # # # # # # # # # # # # # # # #         result = func(*args, **kwargs)

# # # # # # # # # # # # # # # # #         print(f"Execution time: {time.perf_counter() - start:.4f}s")

# # # # # # # # # # # # # # # # #         return result

# # # # # # # # # # # # # # # # #     return wrapper

# # # # # # # # # # # # # # # # # @timer_decorator
# # # # # # # # # # # # # # # # # def slow_math(a, b):
# # # # # # # # # # # # # # # # #     print("called")
# # # # # # # # # # # # # # # # #     time.sleep(1)
# # # # # # # # # # # # # # # # #     return "Done :" + str(a - b)

# # # # # # # # # # # # # # # # # # slow_math = timer_decorator(slow_math)

# # # # # # # # # # # # # # # # # slow_math(1, 2)



# # # # # # # # # # # # # # # # def fibonacci_gen(limit):
# # # # # # # # # # # # # # # #     a, b = 0, 1
# # # # # # # # # # # # # # # #     count = 0
# # # # # # # # # # # # # # # #     print("Here I'm ")
# # # # # # # # # # # # # # # #     while count < limit:
# # # # # # # # # # # # # # # #         yield a
# # # # # # # # # # # # # # # #         a, b = b, a + b
# # # # # # # # # # # # # # # #         count += 1

# # # # # # # # # # # # # # # # # This does NOT store 1 million numbers in RAM

# # # # # # # # # # # # # # # # for num in fibonacci_gen(1000000):
# # # # # # # # # # # # # # # #     if num > 100: break
# # # # # # # # # # # # # # # #     print(num)

# # # # # # # # # # # # # # # #     #    f(n) = f(n-1) + f(n-2)



# # # # # # # # # # # # # # # import random

# # # # # # # # # # # # # # # def image_batch_generator(batch_size):
# # # # # # # # # # # # # # #     while True:
# # # # # # # # # # # # # # #         # Simulate loading images from disk
# # # # # # # # # # # # # # #         batch = [f"Image_Data_{random.randint(1, 100)}" for _ in range(batch_size)]
# # # # # # # # # # # # # # #         yield batch  # Yields a batch, then waits for the next request

# # # # # # # # # # # # # # # # AI Training Loop
# # # # # # # # # # # # # # # loader = image_batch_generator(32)
# # # # # # # # # # # # # # # for i in range(3):
# # # # # # # # # # # # # # #     print(f"Training on: {next(loader)}")
# # # # # # # # # # # # # # #     print()

# # # # # # # # # # # # # # #!/usr/bin/env python3
# # # # # # # # # # # # # # # -*- coding: utf-8 -*-
# # # # # # # # # # # # # # """
# # # # # # # # # # # # # # Created on Fri Mar 13 09:26:35 2026

# # # # # # # # # # # # # # @author: awais
# # # # # # # # # # # # # # """

# # # # # # # # # # # # # # # Generator

# # # # # # # # # # # # # # def ucp_range(size):
# # # # # # # # # # # # # #     count = 0
# # # # # # # # # # # # # #     while count < size:
# # # # # # # # # # # # # #         print("generating: ", str(count))
# # # # # # # # # # # # # #         yield count
# # # # # # # # # # # # # #         count += 1
        

# # # # # # # # # # # # # # for i in ucp_range(100):
# # # # # # # # # # # # # #     print(i)
# # # # # # # # # # # # # # print(ucp_range(10))
# # # # # # # # # # # # # # print(range(100))

# # # # # # # # # # # # # # List comprehension
# # # # # # # # # # # # # # a = [x * 2 for x in range(5)]

# # # # # # # # # # # # # # # Generator expression
# # # # # # # # # # # # # # b = (x * 2 for x in range(5))

# # # # # # # # # # # # # # for _ in a:
# # # # # # # # # # # # # #     print(_)

# # # # # # # # # # # # # # print()
# # # # # # # # # # # # # # for _ in b:

# # # # # # # # # # # # # #     print(_)

# # # # # # # # # # # # # x = "global"

# # # # # # # # # # # # # def outer():
# # # # # # # # # # # # #     x = "enclosing"
# # # # # # # # # # # # #     def inner():
# # # # # # # # # # # # #         global x
# # # # # # # # # # # # #         x = "local" 
# # # # # # # # # # # # #         print("1: ", x) # Searches L -> E -> G -> B
# # # # # # # # # # # # #         if True:
# # # # # # # # # # # # #             x = "inside if"
# # # # # # # # # # # # #             print("2: ", x)
# # # # # # # # # # # # #         print("3: ", x)
# # # # # # # # # # # # #     inner()
# # # # # # # # # # # # #     print("4: ", x)

# # # # # # # # # # # # # outer()
# # # # # # # # # # # # # print("5: ", x)


# # # # # # # # # # # # class A:
# # # # # # # # # # # #     def show(self):
# # # # # # # # # # # #         print("A")


# # # # # # # # # # # # class B(A):
# # # # # # # # # # # #     # def show(self):
# # # # # # # # # # # #     #     print("B")
# # # # # # # # # # # #     ...


# # # # # # # # # # # # class C(A):
# # # # # # # # # # # #     # def show(self):
# # # # # # # # # # # #     #     print("C")
# # # # # # # # # # # #     ...

# # # # # # # # # # # # class D(B, C):
# # # # # # # # # # # #     pass


# # # # # # # # # # # # obj = D()
# # # # # # # # # # # # obj.show()
# # # # # # # # # # # # print(D.mro())



# # # # # # # # # # # class A:
# # # # # # # # # # #     pass

# # # # # # # # # # # class B:
# # # # # # # # # # #     pass

# # # # # # # # # # # class X(A, B):
# # # # # # # # # # #     pass

# # # # # # # # # # # class Y(B, A):
# # # # # # # # # # #     pass

# # # # # # # # # # # class Z(X, Y):
# # # # # # # # # # #     pass


# # # # # # # # # # class A:
# # # # # # # # # #     def show(self):
# # # # # # # # # #         print("A")


# # # # # # # # # # class B(A):
# # # # # # # # # #     def show(self):
# # # # # # # # # #         print("B")
# # # # # # # # # #         super().show()


# # # # # # # # # # class C(A):
# # # # # # # # # #     def show(self):
# # # # # # # # # #         print("C")
# # # # # # # # # #         super().show()


# # # # # # # # # # class D(B, C):
# # # # # # # # # #     def show(self):
# # # # # # # # # #         print("D")
# # # # # # # # # #         super().show()


# # # # # # # # # # obj = D()
# # # # # # # # # # print(D.mro())
# # # # # # # # # # obj.show()


# # # # # # # # # class A:
# # # # # # # # #     def __init__(self, name, age):
# # # # # # # # #         self.name = name
# # # # # # # # #         self.age = age
    
# # # # # # # # #     def __setattr__(self, name, age):
# # # # # # # # #         if name == "age" and age < 0:
# # # # # # # # #             raise ValueError("Age cannot be negative")

# # # # # # # # #         object.__setattr__(self, name, age)

# # # # # # # # # a = A("IMRAN", 21)

# # # # # # # # # print(a.name)
# # # # # # # # # print(a.age)

# # # # # # # # class MyContext:
# # # # # # # #     def __enter__(self):
# # # # # # # #         print("Enter")
# # # # # # # #         return self

# # # # # # # #     def __exit__(self, exc_type, exc_value, traceback):
# # # # # # # #         print("Exit")
# # # # # # # #         print(exc_type)
# # # # # # # #         print(exc_value)
# # # # # # # #         print(traceback)
# # # # # # # #         return True

# # # # # # # # with MyContext():
# # # # # # # #     print("Inside")
# # # # # # # #     raise ValueError("ERROR")

# # # # # # # class Person:
# # # # # # #     def __init__(self):
# # # # # # #         self.name = "IMRAN"
# # # # # # #         self.age = 21

# # # # # # #     def serialization(self):
# # # # # # #         return self.__dict__

# # # # # # # p = Person()

# # # # # # # print(type(p.serialization()))

# # # # # # class A:
# # # # # #     def process(self):
# # # # # #         print("A")


# # # # # # class LoggingMixin:
# # # # # #     def process(self):
# # # # # #         print("Logging")
# # # # # #         super().process()


# # # # # # class ValidationMixin:
# # # # # #     def process(self):
# # # # # #         print("Validation")
# # # # # #         super().process()


# # # # # # class User(LoggingMixin, ValidationMixin, A):
# # # # # #     pass

# # # # # # a = User()
# # # # # # print(User.mro())
# # # # # # a.process()




# # # # # def my_decorator(func):
# # # # #     x = "IMRAN"
# # # # #     def khizer(*args, **kwargs):
# # # # #         print("Hello Khizer!")
# # # # #         print(x)
# # # # #         result = func(*args, **kwargs)
# # # # #         return result
# # # # #     return khizer

# # # # # # @my_decorator
# # # # # def A(a , b, name, age):
# # # # #     print("Performing Calculation on A")
# # # # #     print(a, b, name, age)
# # # # #     return "TRUE BRO"



# # # # # new_A = my_decorator(A)

# # # # # result = new_A("IMRAN", 12, name='IMRAN', age=21)
# # # # # print(result)

# # # # # # lst = [1,2,3,4,5]


# # # # # # def b(*a, **kwargs):
# # # # # #     print(a)
# # # # # #     print(kwargs)

# # # # # # kwagrs = {
# # # # # #     'name': 'imran',
# # # # # #     'age': 12
# # # # # # }

# # # # # # b(*lst, **kwagrs)

# # # # # # print(*lst) # print(1,2,3,4,5)
# # # # # # new_A = my_decorator(A)

# # # # # # A()


# # # # class A:
# # # #     def show(self):
# # # #         print("A")
# # # #     ...

# # # # class  B(A):
# # # #     def show(self):
# # # #         print('B')
# # # #     pass

# # # # class C(B):
# # # #     pass
# # # #     def show(self):
# # # #         print('C')
# # # # class D(C):
# # # #     pass

# # # # d = D()

# # # # d.show()

# # # # print(D.mro())


# # # from ssl import ALERT_DESCRIPTION_BAD_CERTIFICATE_STATUS_RESPONSE
# # # class A:
# # #     def __init__(self):
# # #         print("Constructor")

# # #     def __enter__(self):
# # #         print("Initializing ")
# # #         return self
# # #     def __exit__(self, exc_type, exc_val, exc_tb):
# # #         print("Cleaning Resources!")
# # #         print(exc_type)
# # #         print(exc_val)
# # #         print(exc_tb)
# # #         return True


# # # with A() as a:
    
# # #     print("Working in with!")
# # #     raise ValueError("BEO")


# # def a(dct:dict):
# #     dct['bro'] = 'bro'
# #     # a  = 10
# #     # lst.append(10)

# # # lst = [1,2]

# # dct = {
# #     'imran': 12
# # }

# # a(dct)

# # print(dct)

# import numpy as np

# a = np.array([1,2,3,4])
# # b = arr[0:3]
# # print(b)
# # print(arr)
# # b[2] = 99
# # print(arr)

# print(a[np.array(np.where(a > 2, 1, 0), dtype=bool)])
# # print(np.array([1,2,3,4,5,6,7], dtype=bool))
# # arr = 3 * arr

# import numpy as np 
# x=np.array([10,20,30,40,50]) 
# y = x[1:4] 
# y[0] = 99

# print(x)


# def universal_logger(name, *args, **kwargs):
#     mode = kwargs.get("mode", "standard")
#     total = sum(args)
#     return f"Target: {name} | Mode: {mode} | Total: {total}"
# data = [1, 2, 3] 
# config = {"mode": "silent", "priority" : 1} 
# x = universal_logger("Gamma", *data, **config)
# print(x)

# items = ["Weight", "Color", "Texture", "Size"]
# values = [150, "Red", "Rough"]
# x = []
# for i, v in zip(items, values):
#     x.append((i, v))
# print(x)

import numpy as np

# a = np.array([[1, 2, 3], [4, 5, 6]])
# b = np.array([10, 20, 30])
# x = a + b
# print(x)

data = np.array([[10, 2], [20, 5], [30, 8]])
x = np.sum(data, axis=1)
# print(x)
import random
print(random.uniform(1, 100))