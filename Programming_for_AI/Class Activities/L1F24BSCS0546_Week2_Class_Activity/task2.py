

def summerize(cities, temps, humidity):
    result = [
        f"The Weather in {c} is {t}C with {h}% humidity."
        for c,t,h in zip(cities, temps, humidity)
    ]

    return result


cities = ["Lahore", "Karachi", "Islamabad"]
temps = [32, 35, 28]
humidity = [60, 70, 45]
print(summerize(cities, temps, humidity))
