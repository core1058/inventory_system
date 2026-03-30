class Product:
    #Storing infomation of a single commodity
    def __init__(self, product_id: str, name: str, price: float, quantity: int):
        self._product_id = product_id
        self._name = name
        self.set_price(price)
        self.set_quantity(quantity)

    # Get the product ID
    def get_product_id(self):
        return self._product_id

    # Get the product name
    def get_name(self):
        return self._name

    # Get the product price
    def get_price(self):
        return self._price

    # Set the unit price and must be positive
    def set_price(self, new_price: float):
        if new_price > 0:
            self._price = new_price
        else:
            raise ValueError("Price must be positive.")

    # Get the product quantity
    def get_quantity(self):
        return self._quantity

    # Set the inventory quantity and must be positive
    def set_quantity(self, new_quantity: int):
        if new_quantity >= 0:
            self._quantity = new_quantity
        else:
            raise ValueError("Quantity cannot be negative.")

    #Total value of goods (price * quantity)
    def calculate_value(self) -> float:
        return self._price * self._quantity

    # print product information
    def __str__(self):
        return f"Product(ID: {self._product_id}, Name: {self._name}, Price: ${self._price:.2f}, Stock: {self._quantity})"
