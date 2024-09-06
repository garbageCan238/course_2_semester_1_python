class UninterruptiblePowerSupply:
    def __init__(self, manufacturer=None, brand=None, capacity=None):
        self.manufacturer = manufacturer
        self.brand = brand
        self.capacity = capacity

    def print_info(self):
        print(f"UninterruptiblePowerSupply: manufacturer: {self.manufacturer}, brand: {self.brand}, capacity: {self.capacity}")

class PowerSupplyForSale(UninterruptiblePowerSupply):
    def __init__(self, manufacturer=None, brand=None, capacity=None, price=None):
        super().__init__(manufacturer, brand, capacity)
        self.price = price

    def print_info(self):
        print(f"PowerSupplyForSale: manufacturer: {self.manufacturer}, brand: {self.brand}, capacity: {self.capacity}, price: {self.price}")

def main():
    first = UninterruptiblePowerSupply("Samsung", "Apple", 500)
    first.print_info()

    second = PowerSupplyForSale("Dell", "Hp", 300, 5425)
    second.print_info()

if __name__ == "__main__":
    main()
