class UninterruptiblePowerSupply:
    def __init__(self, manufacturer=None, brand=None, capacity=None):
        self.manufacturer = manufacturer
        self.brand = brand
        self.capacity = capacity

def main():
    power_supply = UninterruptiblePowerSupply()

    power_supply.manufacturer = "Samsung"
    power_supply.brand = "Apple"
    power_supply.capacity = 500

    print(f"manufacturer: {power_supply.manufacturer}, brand: {power_supply.brand}, capacity: {power_supply.capacity}")

if __name__ == "__main__":
    main()