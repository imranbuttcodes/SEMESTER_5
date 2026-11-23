# import numpy as np
# # # # #threed_matrix = np.eye(9)

# # # # # print(threed_matrix)

# # # # a = np.array([
# # # #     [10, 20, 30],
# # # #     [40, 50, 60],
# # # #     [70, 80, 90]
# # # # ])

# # # # # print(a[0:2,1:3])

# # # # print(a.flatten())
# # # # print(a.ravel())
# # # # print(a.sum(axis=0))
# # # # print(np.sum(a, axis=0))

# # # a = np.array([[1, 2, 3],
# # #               [4, 5, 6]])

# # # b = np.array([[10, 20, 30], [21,31,41]])

# # # # print(a + b)

# # # # a = np.array([10, 20, 30, 20, -10])

# # # # print(np.unique(a))
# # # # print(np.argmax(a))
# # # # print(np.where(a > 10))
# # # # print(np.concatenate((a, b), axis=1))
# # # a=np.array([1,2,3,4,5])
# # # b=np.linspace(2,187, 5)
# # # print(b)
# # # print()
# # # # print(a)
# # # # print(np.split(a, 2))
# # # print(np.vstack((a, b)))

# # a = np.array([10, 20, 30])
# # b = a

# # b[0] = 999

# # print(a)  # [999  20  30]
# # print(b)  # [999  20  30]

# # print(a is b)  # False


# a = np.array([[1, 2, 3], [4, 5, 6]])
# # b = a.view()


# a.shape = (3, 2)

# # print(a.shape)  # (2, 3)
# # print(a)

# # print(b.shape)  # (3, 2)

# print(np.random.rand())       # One random number
# print(np.random.rand(5))      # 1D array of 5 values
# print()
# print(np.random.rand(2, 3))   # 2D array: 2 rows, 3 columns

# # print(np.random.bytes(1))
# print()
# print(np.random.random((2,3)))
# print(np.random.randint(1,100, size=(3,3)))
# print()
# print()
# print(np.random.rand(2,2,2))
# print()
# print(np.random.normal(loc=50, scale=2,size=(2,3)))

# a = [1,2,3,4,5,6,7,8,9,10]

# print(np.random.choice(a))

# print(np.random.shuffle(a))
# print(a)

# np.random.seed(42)

# print(np.random.randint(1, 100, size=6))


from numpy.testing import assert_array_max_ulp
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

data = np.array([[10,2], 
                 [20,5],
                 [30, 8]])
print(np.sum(data, axis=0))