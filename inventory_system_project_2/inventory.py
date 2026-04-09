from typing import List, Dict, Optional
from product import Product

# Inventory management (addition, deletion, update, query)
class Inventory:
    #show the total number of add_product function used for the whole class
    addProductCount = 0
   # Store all the goods in a dictionary
    def __init__(self):
        self._products: Dict[str, Product] = {}
        self.numberOfProduct = 0

    @classmethod
    def increaseAddProductCount(cls):
        cls.addProductCount += 1
    
    # add new products, but the ID cannot be duplicated
    def add_product(self, product: Product) -> None:
        if product.get_product_id() in self._products:
            raise ValueError(f"Product ID {product.get_product_id()} already exists.")
        self._products[product.get_product_id()] = product
        self.numberOfProduct += 1
        Inventory.increaseAddProductCount()

    # Delete product with ID. Give a reminder if it does not exist
    def remove_product(self, product_id: str) -> None:
        if product_id in self._products:
            del self._products[product_id]
            self.numberOfProduct -= 1
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
    
    #Combine two inventories
    def __add__(self, other: 'Inventory') -> 'Inventory':
        #check the object's class info
        if not isinstance(other, Inventory):
            raise TypeError(f"Cannot add Inventory with {type(other).__name__}")
        # Create a new inventory
        combinedInventory = Inventory()
        # Add all products from self
        for productA in self._products.values():
            # Create a new product copy to avoid modifying original
            new_prod = Product(productA.get_product_id(), productA.get_name(), productA.get_price(), productA.get_quantity())
            #add all the product from 1st inventory to combinedInventory
            combinedInventory.add_product(new_prod)

        # Add products from 2nd inventory and merge the product's quantities if ID already exists
        for productB in other._products.values():
            productID = productB.get_product_id()
            existing = combinedInventory.get_product(productID)
            if existing:
                new_qty = existing.get_quantity() + productB.get_quantity()
                existing.set_quantity(new_qty)
            else:
                new_prod = Product(productID, productB.get_name(), productB.get_price(), productB.get_quantity())
                combinedInventory.add_product(new_prod)

        Inventory.numberOfProduct = len(combinedInventory._products)
        return combinedInventory
    
    def __str__(self):
        return f"Inventory contains {len(self._products)} products."
    

