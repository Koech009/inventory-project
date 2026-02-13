# ==========================================
# INVENTORY MANAGEMENT SYSTEM
# ==========================================

# Dictionary to store product data
# Structure:
# {
#     "product_name": {"quantity": int, "price": float}
# }
inventory = {
    "suits": {"quantity": 30, "price": 12000}
}


# ==========================================
# INPUT VALIDATION FUNCTIONS
# ==========================================

def get_valid_name(prompt):
    """
    Get a valid product name from the user.
    - Cannot be empty
    - Must contain only letters and spaces
    - Converted to lowercase for consistency
    """
    while True:
        name = input(prompt).strip()

        if not name:
            print("Product name cannot be empty.")
        elif not name.replace(" ", "").isalpha():
            print("Product name should contain only letters and spaces.")
        else:
            return name.lower()


def get_valid_int(prompt):
    """
    Get a valid non-negative integer from the user.
    Prevents crashes from invalid input.
    """
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Value cannot be negative.")
            else:
                return value
        except ValueError:
            print("Please enter a valid integer.")


def get_valid_float(prompt):
    """
    Get a valid non-negative number (float) from the user.
    """
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Value cannot be negative.")
            else:
                return value
        except ValueError:
            print("Please enter a valid number.")


# ==========================================
# INVENTORY FUNCTIONS
# ==========================================

def add_product(name, quantity, price):
    """Add a new product if it does not already exist."""
    if name in inventory:
        print(f"Product '{name}' already exists.")
    else:
        inventory[name] = {"quantity": quantity, "price": price}
        print(f"Product '{name}' added successfully.")


def view_product(name):
    """Display details of a specific product."""
    if name in inventory:
        product = inventory[name]
        print(f"\nProduct: {name}")
        print(f"Quantity: {product['quantity']}")
        print(f"Price: KSh {product['price']:.2f}")
    else:
        print(f"Product '{name}' not found.")


def view_all_products():
    """Display all products in the inventory."""
    if not inventory:
        print("Inventory is empty.")
    else:
        print("\n--- Inventory List ---")
        for name, details in inventory.items():
            print(
                f"{name} | Quantity: {details['quantity']} | Price: KSh {details['price']:.2f}"
            )


def update_quantity(name, quantity):
    """Update the quantity of an existing product."""
    if name in inventory:
        inventory[name]["quantity"] = quantity
        print(f"Product '{name}' quantity updated.")
    else:
        print(f"Product '{name}' not found.")


def remove_product(name):
    """Remove a product from inventory."""
    if name in inventory:
        del inventory[name]
        print(f"Product '{name}' removed.")
    else:
        print(f"Product '{name}' not found.")


# ==========================================
# MAIN MENU LOOP
# ==========================================

while True:
    print("\n====== INVENTORY MENU ======")
    print("1. Add Product")
    print("2. View Product")
    print("3. View All Products")
    print("4. Update Quantity")
    print("5. Remove Product")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == "1":
        name = get_valid_name("Enter product name: ")
        quantity = get_valid_int("Enter quantity: ")
        price = get_valid_float("Enter price: ")
        add_product(name, quantity, price)

    elif choice == "2":
        name = get_valid_name("Enter product name: ")
        view_product(name)

    elif choice == "3":
        view_all_products()

    elif choice == "4":
        name = get_valid_name("Enter product name: ")
        quantity = get_valid_int("Enter new quantity: ")
        update_quantity(name, quantity)

    elif choice == "5":
        name = get_valid_name("Enter product name: ")
        remove_product(name)

    elif choice == "6":
        print("Exiting program...")
        break

    else:
        print("Invalid option. Please choose between 1 and 6.")
