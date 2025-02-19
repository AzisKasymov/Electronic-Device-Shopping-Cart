from device import Device

class Smartphone(Device):
    def __init__(self, name, price, stock, warranty_period, screen_size, battery_life):
        super().__init__(name, price, stock, warranty_period)
        self.screen_size = screen_size
        self.battery_life = battery_life

    def display_info(self):
        super().display_info()
        print(f"Screen Size: {self.screen_size} sm, Battery percent: {self.battery_life} hours")

    def make_call(self):
        print(f"Making a call from {self.name}")

    def install_app(self):
        print(f"Installing an app on {self.name}")
