import math

with open("input.txt") as file:
    lines = file.read().splitlines()

slope = 3
height = len(lines)
width = len(lines[0])
width_factor = ((height - 1) * slope + 1) / width
width_factor = math.ceil(width_factor)

x_index = 0
tree_count = 0
for line in lines:
    if line[x_index] == "#":
        tree_count += 1
    x_index += 3
print(tree_count)

# part two


def count_trees(slopes, lines):
    width = len(lines[0])
    height = len(lines)
    max_slope = max(slopes)
    width_factor = ((height - 1) * max_slope + 1) / width
    width_factor = math.ceil(width_factor)
    lines = [line * width_factor for line in lines]
    x_indices = [0] * len(slopes)
    tree_counts = [0] * len(slopes)

    for line in lines:
        for i in range(len(x_indices)):
            if float(x_indices[i]).is_integer():
                if line[int(x_indices[i])] == "#":
                    tree_counts[i] += 1
            x_indices[i] += slopes[i]
    return tree_counts


slopes = [1, 3, 5, 7, 0.5]
tree_counts = count_trees(slopes, lines)
print(tree_counts)
result = 1

for num in tree_counts:
    result *= num
print(result)
