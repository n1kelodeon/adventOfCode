def find_first_num(nums: [int], preamble_length: int) -> int:
    preamble = nums[:preamble_length]
    nums = nums[preamble_length:]
    for num in nums:
        adds_up = False
        for i, summand_1 in enumerate(preamble):
            for j, summand_2 in enumerate(preamble):
                if i != j and summand_1 + summand_2 == num:
                    adds_up = True
        if not adds_up:
            return num
        preamble = preamble[1:] + [num]


def find_cont_nums(nums: [int], first_num: int) -> [int]:
    # TODO: Make algorithm more efficient
    cont_nums = []
    i = 0
    start_index = 0
    size = len(nums)
    while i < size:
        cont_nums.append(nums[i])
        if len(cont_nums) == 1:
            i += 1
            continue
        cont_sum = sum(cont_nums)
        if cont_sum == first_num:
            return cont_nums
        elif cont_sum < first_num:
            i += 1
        elif cont_sum > first_num:
            cont_nums = []
            start_index += 1
            i = start_index


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        lines = file.read().splitlines()

    nums = [int(num) for num in lines]
    first_num = find_first_num(nums, preamble_length=25)
    print("Part 1", first_num)

    cont_nums = find_cont_nums(nums, first_num)
    print(cont_nums)
    print("Part 2", min(cont_nums) + max(cont_nums))