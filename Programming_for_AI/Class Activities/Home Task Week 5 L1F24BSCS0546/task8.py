
import sys
import time


def generate_matrix_eager(n):

    matrix = []

    for i in range(n):
        matrix.append([i, i * 0.5, i ** 2])

    return matrix


def stream_matrix_lazy(n):

    for i in range(n):
        yield [i, i * 0.5, i ** 2]


N = 1_000_000


start_time = time.perf_counter()

eager_matrix = generate_matrix_eager(N)

eager_time = time.perf_counter() - start_time

eager_memory = sys.getsizeof(eager_matrix)


start_time = time.perf_counter()

lazy_matrix = stream_matrix_lazy(N)

lazy_time = time.perf_counter() - start_time

lazy_memory = sys.getsizeof(lazy_matrix)



print("MEMORY COMPARISON")
print("-----------------")

print(f"Eager List Memory: {eager_memory:,} bytes")
print(f"Lazy Generator Memory: {lazy_memory:,} bytes")


print("\nINITIAL EXECUTION DELAY")
print("-----------------------")

print(f"Eager Generation Time: {eager_time:.6f} seconds")
print(f"Lazy Generator Creation Time: {lazy_time:.6f} seconds")



start_time = time.perf_counter()

first_eager = eager_matrix[0]

eager_first_time = time.perf_counter() - start_time


start_time = time.perf_counter()

first_lazy = next(lazy_matrix)

lazy_first_time = time.perf_counter() - start_time


print("\nFIRST ELEMENT RETRIEVAL")
print("-----------------------")

print("Eager First Element:", first_eager)
print("Lazy First Element:", first_lazy)

print(f"Eager Retrieval Time: {eager_first_time:.8f} seconds")
print(f"Lazy Retrieval Time: {lazy_first_time:.8f} seconds")
