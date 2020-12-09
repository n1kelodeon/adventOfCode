with open("input.txt") as file:
    seats = file.read().splitlines()


def get_seat_id(seat):
    first_number = seat[:7]
    first_number = first_number.replace("F", "0")
    first_number = first_number.replace("B", "1")
    first_number = int(first_number, 2)
    second_number = seat[7:]
    second_number = second_number.replace("L", "0")
    second_number = second_number.replace("R", "1")
    second_number = int(second_number, 2)
    return first_number * 8 + second_number


maximum_id = 0
for seat in seats:
    id = get_seat_id(seat)
    if id > maximum_id:
        maximum_id = id

print(maximum_id)

# part two
def get_seat_num(seat):
    seat = seat.replace("F", "0")
    seat = seat.replace("B", "1")
    seat = seat.replace("L", "0")
    seat = seat.replace("R", "1")
    seat = int(seat, 2)
    return seat


nums = set(range(8, 1024 - 8))
for seat in seats:
    nums.discard(get_seat_num(seat))

print(nums)
# solution is the seat number, which is missing in between two seats