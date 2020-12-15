import re


class Ship:
    """A ship moving on a x-y coordinate system
    having an orientation in degrees
    """

    def __init__(self):
        self._reset()

    def _reset(self):
        self._orientation = 0
        self._x = 0
        self._y = 0
        self._instructions = list()

    def _calculate_manhatten_distance(self):
        return abs(self._x) + abs(self._y)

    def _parse_instructions(self, nav_instructions):
        for instruction in nav_instructions:
            action, value = re.match("(N|S|E|W|L|R|F)([0-9]+)", instruction).groups()
            self._instructions.append((action, int(value)))

    def _change_orientation(self, orientation):
        self._orientation = (self._orientation + orientation) % 360

    def _move_forward(self, value):
        if self._orientation == 0:
            self._move_east(value)
        elif self._orientation == 90:
            self._move_north(value)
        elif self._orientation == 180:
            self._move_west(value)
        elif self._orientation == 270:
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
                self._change_orientation(value)
            elif action == "R":
                self._change_orientation(-value)
            elif action == "F":
                self._move_forward(value)

    def navigate(self, nav_instructions: list[str]):
        self._reset()
        self._parse_instructions(nav_instructions)
        self._execute_instructions()
        return self._calculate_manhatten_distance()
