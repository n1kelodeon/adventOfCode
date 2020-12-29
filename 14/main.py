import re
from itertools import product


def to_binary(integer: int) -> list[str]:
    return list(f"{integer:036b}")


def to_integer(bits: list[str]) -> int:
    return int("".join(bits), 2)


def parse_input(input: list[str]):
    """Parse input and return list of programs

    Args:
        input (list[str]): input as lines of str

    Returns:
        list: list of programs where each program consists of a bitmask
              and a list of memory write instructions (address, value)
    """
    programs = []
    program = None
    for line in lines:
        if line.startswith("mask"):
            programs.append(program)
            program = []
            mask = re.match("mask = ((X|0|1)+)", line).group(1)
            program.append(mask)
        if line.startswith("mem"):
            address, value = re.match("mem\[([0-9]+)\] = ([0-9]+)", line).groups()
            program.append((int(address), int(value)))
    programs.append(program)
    programs.pop(0)
    return programs


def execute_programs_1(programs):
    results = {}
    for program in programs:
        mask = program[0]
        for address, value in program[1:]:
            value_bits = to_binary(value)
            for i in range(36):
                if mask[i] != "X":
                    value_bits[i] = mask[i]
            results[address] = to_integer(value_bits)
    return results


def execute_programs_2(programs):
    results = {}
    for program in programs:
        mask = program[0]
        for address, value in program[1:]:
            address_bits = to_binary(address)
            floating_bit_indices = []
            for i in range(36):
                if mask[i] == "1":
                    address_bits[i] = "1"
                elif mask[i] == "X":
                    floating_bit_indices.append(i)
            for permutation in product("01", repeat=len(floating_bit_indices)):
                for i, bit_index in enumerate(floating_bit_indices):
                    address_bits[bit_index] = permutation[i]
                results[to_integer(address_bits)] = value
    return results


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        lines = file.read().splitlines()

    programs = parse_input(lines)

    results = execute_programs_1(programs)
    print("Part 1:", sum(results.values()))

    results = execute_programs_2(programs)
    print("Part 2:", sum(results.values()))
