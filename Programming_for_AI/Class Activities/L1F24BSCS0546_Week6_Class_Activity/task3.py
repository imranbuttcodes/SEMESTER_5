class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ShippingMixin:
    def __init__(self, weight):
        self.weight = weight

    def calculate_freight(self):
        return max(10, self.weight * 10)


class DiscountMixin:
    def apply_discount(self, percent):
        self.price -= self.price * (percent / 100)


class Laptop(Product, ShippingMixin, DiscountMixin):

    def __init__(self, name, price, weight):
        Product.__init__(self, name, price)
        ShippingMixin.__init__(self, weight)


macbook = Laptop(name="Macbook Air", price=1200, weight=1.2)

macbook.apply_discount(10)

print("Product:", macbook.name)
print("Price after discount:", macbook.price)
print("Weight:", macbook.weight)
print("Shipping Cost:", macbook.calculate_freight())