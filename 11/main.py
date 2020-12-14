from ferry import Ferry


if __name__ == "__main__":
    with open("11/test_input.txt", "r") as file:
        seat_layout = file.read().splitlines()

    ferry = Ferry(seat_layout)
    ferry.simulate_seating()
    occupied_count = ferry.count_occupied_seats()
    print("Part 1:", occupied_count)
