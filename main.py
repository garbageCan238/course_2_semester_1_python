import random
import time
import copy

class UninterruptiblePowerSupply:
    possible_manufacturers = ["Apple", "Samsung", "Hp", "Dell", "Xiaomi", "Huawei", "Techno", "Google", "OnePlus", "Alcatel", "Asus", "Lenovo", "Vivo"]
    possible_brands = ["S1", "S2", "S3", "Redmi", "Nova", "Spark", "A60", "Go", "K15", "Galaxy", "15", "13", "B256"]

    def __init__(self):
        self.manufacturer = random.choice(self.possible_manufacturers)
        self.brand = random.choice(self.possible_brands)
        self.capacity = random.randint(0, 100_000)

    def __repr__(self):
        return f"UninterruptiblePowerSupply(manufacturer={self.manufacturer}, brand={self.brand}, capacity={self.capacity})"


class PowerSupplies:
    def __init__(self, count):
        self.supplies = [UninterruptiblePowerSupply() for _ in range(count)]

    @property
    def count(self):
        return len(self.supplies)

    def __getitem__(self, index):
        return self.supplies[index]

    def __setitem__(self, index, value):
        self.supplies[index] = value

    def selection_sort(self, compare):
        for j in range(self.count - 1):
            min_idx = j
            for i in range(j + 1, self.count):
                if compare(self.supplies[min_idx], self.supplies[i]):
                    min_idx = i
            self.supplies[j], self.supplies[min_idx] = self.supplies[min_idx], self.supplies[j]

    def bubble_sort(self, compare):
        for j in range(self.count - 1):
            for i in range(self.count - 1):
                if compare(self.supplies[i], self.supplies[i + 1]):
                    self.supplies[i], self.supplies[i + 1] = self.supplies[i + 1], self.supplies[i]

    def shaker_sort(self, compare):
        is_swapped = True
        start = 0
        end = self.count

        while is_swapped:
            is_swapped = False
            for i in range(start, end - 1):
                if compare(self.supplies[i], self.supplies[i + 1]):
                    self.supplies[i], self.supplies[i + 1] = self.supplies[i + 1], self.supplies[i]
                    is_swapped = True
            if not is_swapped:
                break
            is_swapped = False
            end -= 1
            for i in range(end - 1, start - 1, -1):
                if compare(self.supplies[i], self.supplies[i + 1]):
                    self.supplies[i], self.supplies[i + 1] = self.supplies[i + 1], self.supplies[i]
                    is_swapped = True
            start += 1

    def shell_sort(self, compare):
        interval = self.count // 2
        while interval > 0:
            for i in range(interval, self.count):
                temp = self.supplies[i]
                j = i
                while j >= interval and compare(self.supplies[j - interval], temp):
                    self.supplies[j] = self.supplies[j - interval]
                    j -= interval
                self.supplies[j] = temp
            interval //= 2

    def insertion_sort(self, compare):
        for i in range(self.count - 1):
            for j in range(i + 1, 0, -1):
                if compare(self.supplies[j - 1], self.supplies[j]):
                    self.supplies[j], self.supplies[j-1] = self.supplies[j-1], self.supplies[j]


def main():
    count = 5000
    print(f"Sorting {count} power supplies by capacity...")

    original = PowerSupplies(count)
    power_supplies = copy.deepcopy(original)
    start_time = time.time()
    power_supplies.selection_sort(lambda x, y: x.capacity > y.capacity)
    elapsed_time = time.time() - start_time
    print(f"Selection sort, time elapsed: {elapsed_time:.2f} seconds")

    power_supplies = copy.deepcopy(original)
    start_time = time.time()
    power_supplies.bubble_sort(lambda x, y: x.capacity > y.capacity)
    elapsed_time = time.time() - start_time
    print(f"Bubble sort, time elapsed: {elapsed_time:.2f} seconds")

    power_supplies = copy.deepcopy(original)
    start_time = time.time()
    power_supplies.shaker_sort(lambda x, y: x.capacity > y.capacity)
    elapsed_time = time.time() - start_time
    print(f"Shaker sort, time elapsed: {elapsed_time:.2f} seconds")

    power_supplies = copy.deepcopy(original)
    start_time = time.time()
    power_supplies.shell_sort(lambda x, y: x.capacity > y.capacity)
    elapsed_time = time.time() - start_time
    print(f"Shell sort, time elapsed: {elapsed_time:.2f} seconds")

    power_supplies = copy.deepcopy(original)
    start_time = time.time()
    power_supplies.insertion_sort(lambda x, y: x.capacity > y.capacity)
    elapsed_time = time.time() - start_time
    print(f"Insertion sort, time elapsed: {elapsed_time:.2f} seconds")


if __name__ == "__main__":
    main()
