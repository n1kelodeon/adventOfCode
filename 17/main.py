from pocket_dimension_3 import PocketDimension3
from pocket_dimension_4 import PocketDimension4

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        first_layer = file.read().splitlines()

    pocket_dimension_3 = PocketDimension3(first_layer)
    active_count = pocket_dimension_3.simulate()
    print("Part 1:", active_count)

    pocket_dimension_4 = PocketDimension4(first_layer)
    active_count = pocket_dimension_4.simulate()
    print("Part 2:", active_count)