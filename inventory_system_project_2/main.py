from product import Product
from inventory import Inventory
from user import AdminUser
from gui import InventoryGUI
import tkinter as tk

def main():
    inventory = Inventory()
    admin = AdminUser("admin_user")

    try:
        p1 = Product("P001", "Laptop", 999.99, 10)
        p2 = Product("P002", "Mouse", 25.50, 50)
        p3 = Product("P003", "Keyboard", 45.00, 30)
        inventory.add_product(p1)
        inventory.add_product(p2)
        inventory.add_product(p3)
    except ValueError as e:
        print(f"Error initializing products: {e}")

    root = tk.Tk()
    app = InventoryGUI(root, inventory, admin)
    root.mainloop()

if __name__ == "__main__":
    main()