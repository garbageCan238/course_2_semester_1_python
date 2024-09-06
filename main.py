class UninterruptiblePowerSupply:
    def __init__(self, manufacturer=None, brand=None, capacity=None):
        self.manufacturer = manufacturer
        self.brand = brand
        self.capacity = capacity

def main():
    first = UninterruptiblePowerSupply()
    first.manufacturer = "Samsung"
    first.brand = "Apple"
    first.capacity = 500

    print(f"first object: manufacturer: {first.manufacturer}, brand: {first.brand}, capacity: {first.capacity}")

    second = UninterruptiblePowerSupply("Dell", "Hp", 800)
    print(f"second object: manufacturer: {second.manufacturer}, brand: {second.brand}, capacity: {second.capacity}")

if __name__ == "__main__":
    main()