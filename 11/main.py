from ferry import Ferry, Ferry2


if __name__ == "__main__":
    with open("11/input.txt", "r") as file:
        seat_layout = file.read().splitlines()

    ferry = Ferry(seat_layout)
    ferry.simulate_seating()
    occupied_count = ferry.count_occupied_seats()
    print("Part 1:", occupied_count)

    ferry2 = Ferry2(seat_layout)
    ferry2.simulate_seating(occupied_seat_limit=5)
    occupied_count = ferry2.count_occupied_seats()
    print("Part 2:", occupied_count)