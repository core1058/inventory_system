class Product:
    def __init__(self, product_id: str, name: str, price: float, quantity: int):
        self._product_id = product_id
        self._name = name
        self.set_price(price)
        self.set_quantity(quantity)

    def get_product_id(self):
        return self._product_id

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def set_price(self, new_price: float):
        if new_price > 0:
            self._price = new_price
        else:
            raise ValueError("Price must be positive.")

    def get_quantity(self):
        return self._quantity

    def set_quantity(self, new_quantity: int):
        if new_quantity >= 0:
            self._quantity = new_quantity
        else:
            raise ValueError("Quantity cannot be negative.")

    def calculate_value(self) -> float:
        return self._price * self._quantity

    def __str__(self):
        return f"Product(ID: {self._product_id}, Name: {self._name}, Price: ${self._price:.2f}, Stock: {self._quantity})"