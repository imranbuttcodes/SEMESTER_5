
def extract_high_multiples(matrix):
    result = [
        {
            "row": row_idx,
            "col": col_idx,
            "val": item
        }
        for row_idx, row in enumerate(matrix)
        for col_idx,item in enumerate(row)
        if item > 5 and item % 3 == 0
    ]

    return result

matrix = [
    [1,6,2],
    [3,8,7],
    [4,5,9]
]

print(extract_high_multiples(matrix))