class DatasetBatcher:
    def  __init__(self, data, batch_size=2):
        self.current_index = 0
        self.data = data
        self.batch_size = batch_size
    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index >= len(self.data):
            raise StopIteration

        batch = self.data[self.current_index:self.current_index + self.batch_size]
        self.current_index += self.batch_size
        return batch

samples = [101, 102, 103, 104, 105, 106, 107]

batcher = DatasetBatcher(samples, batch_size=3)


print(next(batcher))
print(next(batcher))
print(next(batcher))
