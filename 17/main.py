#%%
from copy import copy
from itertools import product


class PocketDimension:
    def __init__(self, first_layer: list[list[str]]):
        self._cubes = {}
        self._init(first_layer)

    def _init(self, first_layer):
        z = 0
        for y, row in enumerate(first_layer):
            for x, cube in enumerate(row):
                is_active = False
                if cube == "#":
                    is_active = True
                self._cubes[(x, y, z)] = Cube(x, y, z, is_active)

    def _get_cube(self, x, y, z):
        cube = self._cubes.get((x, y, z))
        if cube is None:
            cube = Cube(x, y, z, is_active=False)
            self._cubes[(x, y, z)] = cube
        return cube

    def _count_active_cubes(self):
        active_count = 0
        for cube in self._cubes.values():
            if cube.is_active:
                active_count += 1
        return active_count

    def _update_cube_states(self):
        for cube in self._cubes.values():
            cube.update_state()

    def _add_all_neighbors(self):
        for cube in copy(self._cubes).values():
            for x, y, z in cube.get_all_neighbor_coords():
                self._get_cube(x, y, z)

    def simulate(self):
        for boot_cycle in range(6):
            self._add_all_neighbors()
            for cube in copy(self._cubes).values():
                active_neighbor_count = 0
                for x, y, z in cube.get_all_neighbor_coords():
                    if (x, y, z) not in self._cubes:
                        continue
                    if self._get_cube(x, y, z).is_active:
                        active_neighbor_count += 1
                if cube.is_active and not (2 <= active_neighbor_count <= 3):
                    cube.is_active_next = False
                elif not cube.is_active and active_neighbor_count == 3:
                    cube.is_active_next = True
            self._update_cube_states()
            print(f"Done with cycle {boot_cycle}!")
        return self._count_active_cubes()


class Cube:
    def __init__(self, x, y, z, is_active):
        self.x = x
        self.y = y
        self.z = z
        self.is_active = is_active
        self.is_active_next = None

    def _represent(self):
        return f"Cube({self.x}, {self.y}, {self.z}, {self.is_active})"

    def __repr__(self):
        return self._represent()

    def __str__(self):
        return self._represent()

    def update_state(self):
        if self.is_active_next is not None:
            self.is_active = self.is_active_next

    def get_all_neighbor_coords(self):
        coords = set(
            product(
                range(self.x - 1, self.x + 2),
                range(self.y - 1, self.y + 2),
                range(self.z - 1, self.z + 2),
            )
        )
        coords.remove((self.x, self.y, self.z))
        return list(coords)


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        first_layer = file.read().splitlines()
    pocket_dimension = PocketDimension(first_layer)
    active_count = pocket_dimension.simulate()
    print("Part 1:", active_count)
