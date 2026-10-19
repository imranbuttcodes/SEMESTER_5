
def stream_sensor_data(signal_readings, threshold=50.0):
    for index, reading in enumerate(signal_readings):
        if reading > threshold:
            yield (index, reading, "ANOMALY")
        else:
            yield (index, reading, "NORMAL")


def filter_anomalies(generator_stream):
    for index, reading, status in generator_stream:
        if status == "ANOMALY":
            yield (index, reading, status)



readings = [23.4, 55.1, 48.9, 72.3, 12.0, 99.8, 30.5]

sensor_stream = stream_sensor_data(readings, threshold=50.0)
anomaly_stream = filter_anomalies(sensor_stream)

for item in anomaly_stream:
    print(item)