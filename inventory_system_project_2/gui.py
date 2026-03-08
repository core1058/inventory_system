import tkinter as tk
from tkinter import ttk, messagebox
from product import Product
from inventory import Inventory
from user import User, UserRole, AdminUser

class InventoryGUI:
    def __init__(self, root, inventory: Inventory, user: User):
        self.root = root
        self.root.title("Inventory Management System")
        self.root.geometry("800x600")
        self.inventory = inventory
        self.current_user = user
        self.create_widgets()
        self.refresh_product_list()

    def create_widgets(self):
        user_frame = ttk.Frame(self.root, padding="10")
        user_frame.pack(fill=tk.X)
        ttk.Label(user_frame, text=f"Current User: {self.current_user.get_username()} ({self.current_user.get_role().value})").pack(side=tk.LEFT)

        list_frame = ttk.Frame(self.root, padding="10")
        list_frame.pack(fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(list_frame, columns=("ID", "Name", "Price", "Quantity", "Value"), show="headings")
        self.tree.heading("ID", text="Product ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Price", text="Price ($)")
        self.tree.heading("Quantity", text="Quantity")
        self.tree.heading("Value", text="Total Value ($)")
        self.tree.column("ID", width=100)
        self.tree.column("Name", width=150)
        self.tree.column("Price", width=100)
        self.tree.column("Quantity", width=100)
        self.tree.column("Value", width=120)
        self.tree.pack(fill=tk.BOTH, expand=True)

        control_frame = ttk.Frame(self.root, padding="10")
        control_frame.pack(fill=tk.X)

        add_frame = ttk.LabelFrame(control_frame, text="Add New Product", padding="5")
        add_frame.pack(fill=tk.X, pady=5)
        ttk.Label(add_frame, text="ID:").grid(row=0, column=0, sticky=tk.W)
        self.add_id_entry = ttk.Entry(add_frame)
        self.add_id_entry.grid(row=0, column=1, padx=5)
        ttk.Label(add_frame, text="Name:").grid(row=0, column=2, sticky=tk.W)
        self.add_name_entry = ttk.Entry(add_frame)
        self.add_name_entry.grid(row=0, column=3, padx=5)
        ttk.Label(add_frame, text="Price:").grid(row=0, column=4, sticky=tk.W)
        self.add_price_entry = ttk.Entry(add_frame)
        self.add_price_entry.grid(row=0, column=5, padx=5)
        ttk.Label(add_frame, text="Quantity:").grid(row=0, column=6, sticky=tk.W)
        self.add_quantity_entry = ttk.Entry(add_frame)
        self.add_quantity_entry.grid(row=0, column=7, padx=5)
        self.add_btn = ttk.Button(add_frame, text="Add Product", command=self.add_product)
        self.add_btn.grid(row=0, column=8, padx=5)

        update_frame = ttk.LabelFrame(control_frame, text="Update / Remove Product", padding="5")
        update_frame.pack(fill=tk.X, pady=5)
        ttk.Label(update_frame, text="Product ID:").grid(row=0, column=0, sticky=tk.W)
        self.update_id_entry = ttk.Entry(update_frame)
        self.update_id_entry.grid(row=0, column=1, padx=5)
        ttk.Label(update_frame, text="New Quantity:").grid(row=0, column=2, sticky=tk.W)
        self.update_quantity_entry = ttk.Entry(update_frame)
        self.update_quantity_entry.grid(row=0, column=3, padx=5)
        self.update_btn = ttk.Button(update_frame, text="Update Quantity", command=self.update_product)
        self.update_btn.grid(row=0, column=4, padx=5)
        self.remove_btn = ttk.Button(update_frame, text="Remove Product", command=self.remove_product)
        self.remove_btn.grid(row=0, column=5, padx=5)

        self.total_value_label = ttk.Label(self.root, text="Total Inventory Value: $0.00", padding="10")
        self.total_value_label.pack()
        self.set_button_permissions()

    def set_button_permissions(self):
        if not self.current_user.can_perform_action("add"):
            self.add_btn.config(state=tk.DISABLED)
        if not self.current_user.can_perform_action("update"):
            self.update_btn.config(state=tk.DISABLED)
        if not self.current_user.can_perform_action("remove"):
            self.remove_btn.config(state=tk.DISABLED)

    def refresh_product_list(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for product in self.inventory.list_all_products():
            self.tree.insert("", tk.END, values=(
                product.get_product_id(),
                product.get_name(),
                f"{product.get_price():.2f}",
                product.get_quantity(),
                f"{product.calculate_value():.2f}"
            ))
        total = self.inventory.calculate_total_value()
        self.total_value_label.config(text=f"Total Inventory Value: ${total:.2f}")

    def add_product(self):
        try:
            product_id = self.add_id_entry.get().strip()
            name = self.add_name_entry.get().strip()
            price = float(self.add_price_entry.get().strip())
            quantity = int(self.add_quantity_entry.get().strip())
            if not product_id or not name:
                messagebox.showerror("Error", "Product ID and Name cannot be empty.")
                return
            product = Product(product_id, name, price, quantity)
            self.inventory.add_product(product)
            self.refresh_product_list()
            self.add_id_entry.delete(0, tk.END)
            self.add_name_entry.delete(0, tk.END)
            self.add_price_entry.delete(0, tk.END)
            self.add_quantity_entry.delete(0, tk.END)
            messagebox.showinfo("Success", "Product added successfully!")
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {str(e)}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_product(self):
        try:
            product_id = self.update_id_entry.get().strip()
            new_quantity = int(self.update_quantity_entry.get().strip())
            self.inventory.update_product_quantity(product_id, new_quantity)
            self.refresh_product_list()
            self.update_id_entry.delete(0, tk.END)
            self.update_quantity_entry.delete(0, tk.END)
            messagebox.showinfo("Success", "Product quantity updated!")
        except (ValueError, KeyError) as e:
            messagebox.showerror("Error", str(e))

    def remove_product(self):
        try:
            product_id = self.update_id_entry.get().strip()
            self.inventory.remove_product(product_id)
            self.refresh_product_list()
            self.update_id_entry.delete(0, tk.END)
            self.update_quantity_entry.delete(0, tk.END)
            messagebox.showinfo("Success", "Product removed successfully!")
        except KeyError as e:
            messagebox.showerror("Error", str(e))