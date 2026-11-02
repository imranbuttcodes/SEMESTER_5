
class SlidingWindowIterator:

    def __init__(self, sequence, window_size, step=1):

        self.sequence = sequence
        self.window_size = window_size
        self.step = step

       
        self.start_idx = 0

    def __iter__(self):

        return self

    def __next__(self):

        
        end_idx = self.start_idx + self.window_size

        if end_idx > len(self.sequence):

            raise StopIteration

        window = self.sequence[self.start_idx:end_idx]

        self.start_idx += self.step

        return window


timeseries = [10, 20, 30, 40, 50, 60, 70, 80]

window_iterator = SlidingWindowIterator(
    timeseries,
    window_size=3,
    step=2
)

print("Generated Windows:")

for window in window_iterator:

    print(window)
