class Seat:
    def __init__(self, coordinates: tuple[int, int]):
        self._adjacent_seats = dict()
        self._coordinates = coordinates
        self._is_empty = True

    def add_adjacent_seat(self, seat: "Seat"):
        coords = seat.coordinates
        self._adjacent_seats.update({coords: seat})

    def update(self, is_empty):
        is_updated = False
        if self._is_empty != is_empty:
            self._is_empty = is_empty
            is_updated = True
        return is_updated

    @property
    def coordinates(self):
        return self._coordinates

    @property
    def adjacent_seats(self):
        return self._adjacent_seats

    @property
    def is_empty(self):
        return self._is_empty
