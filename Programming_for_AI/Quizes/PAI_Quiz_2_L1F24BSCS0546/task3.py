def clamp_and_label_signals(readings, lower_bound=-1.0, upper_bound=1.0):

    result = [
        "LOWER_CLAMP" if x < lower_bound else 
        "UPPER_CLAMP" if x > upper_bound else round(x, 2)
        for x in readings
    ]

    return result

print(clamp_and_label_signals([-2.5, -0.456, 0.123, 1.89, 0.999, -1.05]))