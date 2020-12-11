import re

pattern = re.compile("([0-9]+)-([0-9]+) (.): (.+)")
with open("input.txt") as file:
    lines = file.read().splitlines()

valid_count = 0
for line in lines:
    count_min = int(pattern.match(line).group(1))
    count_max = int(pattern.match(line).group(2))
    char = pattern.match(line).group(3)
    passwd = pattern.match(line).group(4)
    if count_min <= passwd.count(char) <= count_max:
        valid_count += 1
print(valid_count)

# part two
valid_count = 0
for line in lines:
    count_min = int(pattern.match(line).group(1))
    count_max = int(pattern.match(line).group(2))
    char = pattern.match(line).group(3)
    passwd = pattern.match(line).group(4)
    appear_count = 0
    if passwd[count_min - 1] == char:
        appear_count += 1
    if passwd[count_max - 1] == char:
        appear_count += 1
    if appear_count == 1:
        valid_count += 1

print(valid_count)
