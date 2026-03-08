from typing import List, Dict, Optional
from product import Product

class Inventory:
    def __init__(self):
        self._products: Dict[str, Product] = {}

    def add_product(self, product: Product) -> None:
        if product.get_product_id() in self._products:
            raise ValueError(f"Product ID {product.get_product_id()} already exists.")
        self._products[product.get_product_id()] = product

    def remove_product(self, product_id: str) -> None:
        if product_id in self._products:
            del self._products[product_id]
        else:
            raise KeyError(f"Product ID {product_id} not found.")

    def update_product_quantity(self, product_id: str, new_quantity: int) -> None:
        if product_id in self._products:
            self._products[product_id].set_quantity(new_quantity)
        else:
            raise KeyError(f"Product ID {product_id} not found.")

    def get_product(self, product_id: str) -> Optional[Product]:
        return self._products.get(product_id)

    def list_all_products(self) -> List[Product]:
        return list(self._products.values())

    def calculate_total_value(self) -> float:
        total = 0.0
        for product in self._products.values():
            total += product.calculate_value()
        return total

    def __str__(self):
        return f"Inventory contains {len(self._products)} products."