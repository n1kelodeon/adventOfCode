from collections import defaultdict


class MemoryGame:
    def __init__(self):
        self._numbers = None
        self._last_num = None
        self._reset()

    def _reset(self):
        self._numbers = defaultdict(list)
        self._last_num = None

    def _init(self, starting_nums: list[int]):
        for turn_id, num in enumerate(starting_nums, start=1):
            self._numbers[num].append(turn_id)
        self._last_num = list(self._numbers)[-1]

    def _calc_age(self, number: int):
        return self._numbers[number][-1] - self._numbers[number][-2]

    def _speak_aloud_number(self, number, turn):
        self._numbers[number].append(turn)
        self._last_num = number

    def play(self, starting_nums: list[int], limit: int) -> int:
        self._reset()
        self._init(starting_nums)
        for turn in range(len(self._numbers) + 1, limit + 1):
            # check if last number was spoken for the first time
            if self._numbers[self._last_num] == [turn - 1]:
                self._speak_aloud_number(0, turn)
            else:
                age = self._calc_age(self._last_num)
                self._speak_aloud_number(age, turn)
        return self._last_num


if __name__ == "__main__":
    with open("15/input.txt", "r") as file:
        starting_nums = [int(x) for x in file.read().split(",")]

    game = MemoryGame()
    last_num = game.play(starting_nums, limit=2020)
    print("Part 1:", last_num)

    last_num = game.play(starting_nums, limit=30000000)
    print("Part 2:", last_num)
