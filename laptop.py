from device import Device

class Laptop(Device):
    def __init__(self, name, price, stock, warranty_period, ram_size, processor_speed):
        super().__init__(name, price, stock, warranty_period)
        self.ram_size = ram_size
        self.processor_speed = processor_speed

    def display_info(self):
        super().display_info()
        print(f"RAM: {self.ram_size}GB, Processor: {self.processor_speed}GHz")

    def run_program(self):
        print(f"Running a program o {self.name}")

    def use_keyboard(self):
        print(f"Typing on {self.name}")
