from ship import Ship, Ship2

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        nav_instructions = file.read().splitlines()

    ship = Ship()
    distance = ship.navigate(nav_instructions)
    print("Part 1", distance)

    ship2 = Ship2()
    distance = ship2.navigate(nav_instructions)
    print("Part 2:", distance)
