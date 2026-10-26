def print_config(model_name, **hyperparams):
    print("Model Name:", model_name)
    print()

    for key, value in hyperparams.items():
        print(f"{key} -> {value}")

print_config("RandomForest", n_estimators=100, max_depth=5, random_state=42)

