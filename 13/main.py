if __name__ == "__main__":
    with open("input.txt", "r") as file:
        timestamp, bus_ids = file.read().splitlines()
        arrival_time = int(timestamp)
        bus_ids = bus_ids.split(",")
        bus_ids = [int(id) for id in bus_ids if id != "x"]

    is_waiting = True
    waiting_time = 0
    while is_waiting:
        waiting_time += 1
        for bus_id in bus_ids:
            if (arrival_time + waiting_time) % bus_id == 0:
                is_waiting = False
                break

    print("Part 1:", bus_id * waiting_time)
