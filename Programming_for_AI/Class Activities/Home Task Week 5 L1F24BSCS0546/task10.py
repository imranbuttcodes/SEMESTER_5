def stream_raw_images(image_records):
    for image_rcd in image_records:

        yield image_rcd


def augment_stream(generator_source):

    for s in generator_source:

        if s['pixels']:
            s['augmented'] = True

            yield s


def normalize_stream(generator_source):

    for s in generator_source:

        if s['pixels']:

            s['pixels'] = [p/225.0 for p in s['pixels']]

            yield s



raw_batch = [
{'image_id': 1, 'pixels': [0, 128, 255]},
{'image_id': 2, 'pixels': []},
{'image_id': 3, 'pixels': [64, 192, 32]}
]


pipeline = normalize_stream(augment_stream(stream_raw_images(raw_batch)))


for p in pipeline:

    print(p)