from seat import Seat
from copy import deepcopy


class Ferry:
    def __init__(self, seat_layout: list[list[str]]):
        self._seats = dict()
        self._dimensions = None
        self._init_seats(seat_layout)

    def _get_seat(self, coordinates: tuple[int, int]) -> "Seat":
        seat = self._seats.get(coordinates)
        if seat is None:
            seat = Seat(coordinates)
            self._seats.update({coordinates: seat})
        return seat

    def _get_adjacent_coords(
        self, coordinates: tuple[int, int], dimensions: tuple[int, int]
    ) -> list[tuple[int, int]]:
        adjacent_coords = list()
        i, j = coordinates
        m, n = dimensions
        # left, right, up, down
        if i > 0:
            adjacent_coords.append((i - 1, j))
        if i < m - 1:
            adjacent_coords.append((i + 1, j))
        if j > 0:
            adjacent_coords.append((i, j - 1))
        if j < n - 1:
            adjacent_coords.append((i, j + 1))
        # diagonals
        if i > 0 and j > 0:
            adjacent_coords.append((i - 1, j - 1))
        if i < m - 1 and j < n - 1:
            adjacent_coords.append((i + 1, j + 1))
        if i > 0 and j < n - 1:
            adjacent_coords.append((i - 1, j + 1))
        if i < m - 1 and j > 0:
            adjacent_coords.append((i + 1, j - 1))
        return adjacent_coords

    def _init_seats(self, seat_layout):
        m, n = len(seat_layout), len(seat_layout[0])
        self._dimensions = (m, n)
        for i in range(m):
            for j in range(n):
                if seat_layout[i][j] == ".":
                    continue
                seat = self._get_seat(coordinates=(i, j))
                adjacent_coords = self._get_adjacent_coords((i, j), (m, n))
                for k, l in adjacent_coords:
                    if seat_layout[k][l] != ".":
                        seat.add_adjacent_seat(self._get_seat((k, l)))

    def simulate_seating(self, print_seat_layout=False):
        if print_seat_layout:
            self.print_seat_layout()
        update_count = 0
        for seat in self._seats.values():
            adjacent_occupied_count = 0
            for adjacent_seat in seat.adjacent_seats.values():
                if not adjacent_seat.is_empty:
                    adjacent_occupied_count += 1
            # occupy seat if there are no occupied adjacent seats
            if seat.is_empty:
                if adjacent_occupied_count == 0:
                    self._seats[seat.coordinates].is_empty_next = False
                    update_count += 1
            # free seat if four or more adjacent seats are occupied
            elif not seat.is_empty:
                if adjacent_occupied_count >= 4:
                    self._seats[seat.coordinates].is_empty_next = True
                    update_count += 1
        self.update_seat_states()
        if update_count > 0:
            return self.simulate_seating()

    def count_occupied_seats(self):
        occupied_count = 0
        for seat in self._seats.values():
            if not seat.is_empty:
                occupied_count += 1
        return occupied_count

    def print_seat_layout(self):
        m, n = self._dimensions
        for i in range(m):
            row = list()
            for j in range(n):
                coords = (i, j)
                if coords in self._seats.keys():
                    if self._seats[coords].is_empty:
                        row.append("L")
                    else:
                        row.append("#")
                else:
                    row.append(".")
            print("".join(row))
        print("\n")

    def update_seat_states(self):
        for seat in self._seats.values():
            seat.update_state()
