from device import Device

class Tablet(Device):
    def __init__(self, name, price, stock, warranty_period, screen_resolution, weight):
        super().__init__(name, price, stock, warranty_period)
        self.screen_resolution = screen_resolution
        self.weight = weight

    def display_info(self):
        super().display_info()
        print(f"Resolution: {self.screen_resolution}, Weight: {self.weight}g")

    def  browse_internet (self):
        print(f"Browsing the internet on {self.name}")

    def use_touchscreen(self):
        print(f"using touchscreen on {self.name}")
