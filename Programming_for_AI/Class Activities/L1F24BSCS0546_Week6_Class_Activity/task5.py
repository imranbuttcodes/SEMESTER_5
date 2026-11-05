class Signal:
    def __init__(self, vec):
        self.vec = vec

    def __len__(self):

        return len(self.vec)
    
    def __add__(self, Other):

        return [self.vec + Other.vec]

    def __getitem__(self, idx):

        return self.vec[idx]

    def __str__(self):

        return f"Signal(Size: {len(self.vec)}, Mean: {(sum(self.vec))/ len(self.vec)})."

        