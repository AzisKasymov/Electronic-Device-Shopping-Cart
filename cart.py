from device import Device

class Cart:
    def __init__(self):
        self.items = []

    def add_device(self, device, amount):
        if device.is_available(amount):
            self.items.append((device, amount))
            device.reduce_stock(amount)
            print(f"added {amount} {device.name} to cart.")
        else:
            print(f"not enough stock for {device.name}.")

    def remove_device(self, device, amount):
        for item in self.items:
            if item[0] == device and item[1] >= amount:
                self.items.remove(item)
                device.stock += amount
                print(f"removed {amount} {device.name} from cart.")
                break
    def calculate_total(self):
        return sum(item[0].price * item[1] for item in self.items)

    def checkout(self):
        total = self.calculate_total()
        print(f"Total amount: ${total:.2f}")
        self.items.clear()
        print("checkout completed,thank!")