class UninterruptiblePowerSupply:
    manufacturer: str
    brand: str
    capacity: int

def main():
    UninterruptiblePowerSupply.manufacturer = "Samsung"
    UninterruptiblePowerSupply.brand = "Apple"
    UninterruptiblePowerSupply.capacity = 500

    print(f"manufacturer: {UninterruptiblePowerSupply.manufacturer}, "
          f"\nbrand: {UninterruptiblePowerSupply.brand}, "
          f"\ncapacity: {UninterruptiblePowerSupply.capacity}"
          )

if __name__ == "__main__":
    main()