def  create_feature_scaler(min_val, max_val):

    def scale(x):
        return (x - min_val) / (max_val - min_val)

    return scale



age_scaler = create_feature_scaler(min_val=18, max_val=65)

grade_scaler = create_feature_scaler(min_val=0, max_val=20)

print(age_scaler(30))

print(grade_scaler(15))

print(age_scaler.__closure__[0].cell_contents)
print(age_scaler.__closure__[1].cell_contents)