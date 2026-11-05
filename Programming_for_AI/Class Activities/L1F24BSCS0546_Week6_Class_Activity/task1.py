class Currency:
    def __init__(self, amount, code):
        self.amount = amount
        self.code = code
    
    def __add__(self, Other):

        if self.code != Other.code:
            raise ValueError(f"Currency Code didn't match with {self.code}")
        
        return Currency(self.amount + Other.amount, self.code)
    
    def __str__(self):

        return f"{self.code} {self.amount}"

    def __repr__(self):
        return f"Currency(amount={self.amount}, code={self.code})"
    


c1 = Currency(500, "USD")
c2 = Currency(300, "USD")


print(c1 + c2)
        