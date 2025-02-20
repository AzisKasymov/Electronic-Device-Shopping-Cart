from smartphone import Smartphone
from laptop import Laptop
from tablet import Tablet
from cart import Cart

devices = [
    Smartphone("iPhone 13", 999, 10, 12, 6.1, 20),
    Laptop("MacBook Pro", 1999, 5, 24, 16, 3.2),
    Tablet("iPad Pro", 799, 8, 12, "2048x1536", 500)
]

cart = Cart()
while True:
    print("\n1. Show Devices\n2. Show Cart\n3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        for idx, device in enumerate(devices, 1):
            print(f"{idx}. ", end="")
            device.display_info()
        item_choice = int(input("Select a device to add to cart (or 0 to cancel): "))
        if item_choice > 0 and item_choice <= len(devices):
            quantity = int(input("Enter quantity: "))
            cart.add_device(devices[item_choice - 1], quantity)
    elif choice == "2":
        if not cart.items:
            print("Cart is empty.")
        else:
            print("Cart Items:")
            for device, qty in cart.items:
                print(f"{device.name} - {qty} units")
            print(f"Total: ${cart.calculate_total():.2f}")
            checkout_choice = input("Proceed to checkout? (yes/no): ")
            if checkout_choice.lower() == "yes":
                cart.checkout()
    elif choice == "3":
        break
    else:
        print("Invalid choice.")
# Output