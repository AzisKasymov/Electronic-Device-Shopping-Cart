from device import Device

class Cart:
    def __init__(self):
        self.items = []

    def add_device(self, device, amount):
        if device.is_available(amount):
            self.items.append((device, amount))
            device.reduce_stock(amount)
            print(f"Added {amount} {device.name} to cart.")
        else:
            print(f"Not enough stock for {device.name}.")

    def remove_device(self, device, amount):
        for item in self.items:
            if item[0] == device and item[1] >= amount:
                self.items.remove(item)
                device.stock += amount
                print(f"Removed {amount} {device.name} from cart.")
                break