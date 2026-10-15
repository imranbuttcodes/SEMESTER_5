import math



def process_coordinates(points, min_dist):

    calculate_distance = lambda point: math.sqrt((int(point.split(":")[1]) - int(point.split(":")[2]))**2)

    result = [        
        tuple(
            (
                point.split(":")[0], calculate_distance(point)
            )
            )            
            for point in points

            if calculate_distance(point) > min_dist
    ]

    result = sorted(result, reverse=True, key=lambda x: x[1])

    final_result = [
        dict(
            {
                i[0]: i[1]
            }
        )
        for i in result
    ]
    return final_result



string_ = ["P1:10:9", "P2:34:5", "P3:45:10"]


print(process_coordinates(string_, 12))
