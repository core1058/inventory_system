from typing import List, Dict, Optional
from product import Product

# Inventory management (addition, deletion, update, query)
class Inventory:
   # Store all the goods in a dictionary
    def __init__(self):
        self._products: Dict[str, Product] = {}

    # add new products, but the ID cannot be duplicated
    def add_product(self, product: Product) -> None:
        if product.get_product_id() in self._products:
            raise ValueError(f"Product ID {product.get_product_id()} already exists.")
        self._products[product.get_product_id()] = product
        
    # Delete product with ID. Give a reminder if it does not exist
    def remove_product(self, product_id: str) -> None:
        if product_id in self._products:
            del self._products[product_id]
        else:
            raise KeyError(f"Product ID {product_id} not found.")

    # Update the quantity of the specified product
    def update_product_quantity(self, product_id: str, new_quantity: int) -> None:
        if product_id in self._products:
            self._products[product_id].set_quantity(new_quantity)
        else:
            raise KeyError(f"Product ID {product_id} not found.")

    # Find products by ID
    def get_product(self, product_id: str) -> Optional[Product]:
        return self._products.get(product_id)

    # Return the list of all products
    def list_all_products(self) -> List[Product]:
        return list(self._products.values())

    # Calculate the total value of the entire inventory
    def calculate_total_value(self) -> float:
        total = 0.0
        for product in self._products.values():
            total += product.calculate_value()
        return total

    def __str__(self):
        return f"Inventory contains {len(self._products)} products."
