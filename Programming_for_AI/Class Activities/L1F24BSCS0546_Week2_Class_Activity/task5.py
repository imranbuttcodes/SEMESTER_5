def combine(keys, values):

    result = {
        key: value
        for key, value in zip(keys, values)
    }

    return result


keys = ["ID", "Name", "Role"] 
values = [101, "Awais", "Faculty"]


print(combine(keys, values))