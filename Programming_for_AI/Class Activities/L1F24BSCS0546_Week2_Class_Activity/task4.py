c_temps = [0, 12, 34, 100, -5, 25]


filter_pos = lambda t: t >= 0

pos_temps = list(filter(filter_pos, c_temps))
print("pos Temps:", pos_temps)

fahrenheit_temp = list(map(lambda c: (c * (9/5) + 32), pos_temps))

print("fahrenheit_temp:",fahrenheit_temp)