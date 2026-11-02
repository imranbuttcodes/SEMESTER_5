from os import PRIO_PGRP
import math

def compress_sparse_vector(dense_vector, threshold=0.01):
    result = [
        (idx, val) 
        for idx, val in enumerate(dense_vector)
        if abs(val) > threshold
    ]

    return result


print(compress_sparse_vector([0.0, 0.85, -0.002, 1.45, 0.0, -0.62, 0.009]))

