with open("input.txt") as file:
    lines = file.read().splitlines()

nums = []
for line in lines:
    nums.append(int(line))


def find_nums_part_one():
    for first_num in nums:
        for sec_num in nums:
            if first_num + sec_num == 2020:
                return first_num, sec_num


a, b = find_nums_part_one()
result = a * b
print(result)


def find_nums_part_two():
    for num_1 in nums:
        for num_2 in nums:
            for num_3 in nums:
                if num_1 + num_2 + num_3 == 2020:
                    return num_1, num_2, num_3


a, b, c = find_nums_part_two()
print(a * b * c)
