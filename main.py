import json
import random


class UninterruptiblePowerSupply:
    possible_manufacturers = ["Apple", "Samsung", "Hp", "Dell", "Xiaomi", "Huawei", "Techno", "Google", "OnePlus",
                              "Alcatel", "Asus", "Lenovo", "Vivo"]
    possible_brands = ["S1", "S2", "S3", "Redmi", "Nova", "Spark", "A60", "Go", "K15", "Galaxy", "15", "13", "B256"]

    def __init__(self):
        self.manufacturer = random.choice(self.possible_manufacturers)
        self.brand = random.choice(self.possible_brands)
        self.capacity = random.randint(0, 1000)

    def print_info(self):
        print(
            f"UninterruptiblePowerSupply: manufacturer: {self.manufacturer}, brand: {self.brand}, capacity: {self.capacity}")


class PowerSupplies:
    def __init__(self, count):
        self.count = count
        self.supplies = [None] * count

    def __getitem__(self, index):
        return self.supplies[index]

    def __setitem__(self, index, value):
        self.supplies[index] = value

    def print_info(self):
        for supply in self.supplies:
            supply.print_info()


def main():
    single_power_supply = UninterruptiblePowerSupply()

    power_supplies = PowerSupplies(5)
    for i in range(power_supplies.count):
        power_supplies[i] = UninterruptiblePowerSupply()

    print("Single: ")
    single_power_supply.print_info()

    print("Container: ")
    power_supplies.print_info()

    with open("single_power_supply.json", "w") as file:
        json.dump(single_power_supply.__dict__, file)

    with open("power_supplies.json", "w") as file:
        json.dump([supply.__dict__ for supply in power_supplies.supplies], file)

    with open("single_power_supply.json", "r") as file:
        data = json.load(file)
        deserialized_single = UninterruptiblePowerSupply()
        deserialized_single.__dict__.update(data)

    with open("power_supplies.json", "r") as file:
        data = json.load(file)
        deserialized_supplies = PowerSupplies(5)
        for i, supply_data in enumerate(data):
            deserialized_supply = UninterruptiblePowerSupply()
            deserialized_supply.__dict__.update(supply_data)
            deserialized_supplies[i] = deserialized_supply

    print("\nDeserialized single: ")
    deserialized_single.print_info()

    print("Deserialized container: ")
    deserialized_supplies.print_info()


if __name__ == "__main__":
    main()
