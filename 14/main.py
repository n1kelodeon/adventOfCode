import re

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        lines = file.read().splitlines()

# fetch programs
programs = []
program = None
for line in lines:
    if "mask" in line:
        programs.append(program)
        program = []
        mask = re.match("mask = ((X|0|1)+)", line).group(1)
        program.append(mask)
    if "mem" in line:
        address, value = re.match("mem\[([0-9]+)\] = ([0-9]+)", line).groups()
        program.append((int(address), int(value)))
programs.append(program)
programs.pop(0)

# execute program as in part 1
results = {}
for program in programs:
    mask = program.pop(0)
    for address, value in program:
        # get list of bits of value
        value_bits = list(f"{value:036b}")
        for i in range(36):
            if mask[i] != "X":
                value_bits[i] = mask[i]
        results[address] = int("".join(value_bits), 2)

print("Part 1:", sum(results.values()))
