import random

class UninterruptiblePowerSupply:
    possible_manufacturers = ["Apple", "Samsung", "Hp", "Dell", "Xiaomi", "Huawei", "Techno", "Google", "OnePlus", "Alcatel", "Asus", "Lenovo", "Vivo"]
    possible_brands = ["S1", "S2", "S3", "Redmi", "Nova", "Spark", "A60", "Go", "K15", "Galaxy", "15", "13", "B256"]

    def __init__(self):
        self.manufacturer = random.choice(self.possible_manufacturers)
        self.brand = random.choice(self.possible_brands)
        self.capacity = random.randint(0, 1000)

class PowerSupplies:
    def __init__(self, count):
        self.count = count
        self.supplies: list[None | UninterruptiblePowerSupply] = [None] * count

    def __getitem__(self, index):
        return self.supplies[index]

    def __setitem__(self, index, value):
        self.supplies[index] = value

def main():
    power_supplies = PowerSupplies(10)
    for i in range(power_supplies.count):
        power_supplies[i] = UninterruptiblePowerSupply()
        print(f"manufacturer: {power_supplies[i].manufacturer}, brand: {power_supplies[i].brand}, capacity: {power_supplies[i].capacity}")

if __name__ == "__main__":
    main()