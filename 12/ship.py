import re


class Ship:
    """A ship moving on a x-y coordinate system
    having an orientation in degrees
    """

    def __init__(self):
        self._angle = None
        self._x = None
        self._y = None
        self._instructions = None
        self._reset()

    def _reset(self):
        self._angle = 0
        self._x = 0
        self._y = 0
        self._instructions = list()

    def _calculate_manhatten_distance(self):
        return abs(self._x) + abs(self._y)

    def _parse_instructions(self, nav_instructions):
        for instruction in nav_instructions:
            action, value = re.match("(N|S|E|W|L|R|F)([0-9]+)", instruction).groups()
            self._instructions.append((action, int(value)))

    def _rotate(self, angle):
        self._angle = (self._angle + angle) % 360

    def _move_forward(self, value):
        if self._angle == 0:
            self._move_east(value)
        elif self._angle == 90:
            self._move_north(value)
        elif self._angle == 180:
            self._move_west(value)
        elif self._angle == 270:
            self._move_south(value)

    def _move_north(self, value):
        self._y += value

    def _move_south(self, value):
        self._y -= value

    def _move_east(self, value):
        self._x += value

    def _move_west(self, value):
        self._x -= value

    def _execute_instructions(self):
        for action, value in self._instructions:
            if action == "N":
                self._move_north(value)
            elif action == "S":
                self._move_south(value)
            elif action == "E":
                self._move_east(value)
            elif action == "W":
                self._move_west(value)
            elif action == "L":
                self._rotate(value)
            elif action == "R":
                self._rotate(-value)
            elif action == "F":
                self._move_forward(value)

    def navigate(self, nav_instructions: list[str]):
        self._reset()
        self._parse_instructions(nav_instructions)
        self._execute_instructions()
        return self._calculate_manhatten_distance()


class Ship2(Ship):
    def __init__(self):
        self._angle = None
        self._x = None
        self._y = None
        self._waypoint_x_offset = None
        self._waypoint_y_offset = None
        self._instructions = None
        self._reset()

    def _reset(self):
        self._angle = 0
        self._x = 0
        self._y = 0
        self._waypoint_x_offset = 10
        self._waypoint_y_offset = 1
        self._instructions = list()

    def _sin(self, angle):
        sinus = {90: 1, 180: 0, 270: -1}
        if angle < 0:
            return -sinus[-angle]
        return sinus[angle]

    def _cos(self, angle):
        cosinus = {90: 0, 180: -1, 270: 0}
        return cosinus[abs(angle)]

    def _rotate(self, angle):
        x, y = self._waypoint_x_offset, self._waypoint_y_offset
        self._waypoint_x_offset = x * self._cos(angle) - y * self._sin(angle)
        self._waypoint_y_offset = x * self._sin(angle) + y * self._cos(angle)

    def _move_forward(self, value):
        self._x += value * self._waypoint_x_offset
        self._y += value * self._waypoint_y_offset

    def _move_north(self, value):
        self._waypoint_y_offset += value

    def _move_south(self, value):
        self._waypoint_y_offset -= value

    def _move_east(self, value):
        self._waypoint_x_offset += value

    def _move_west(self, value):
        self._waypoint_x_offset -= value
