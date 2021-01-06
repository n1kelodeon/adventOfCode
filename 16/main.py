import re


def is_valid_value(value, intervals):
    interval_1, interval_2 = intervals
    return (
        interval_1[0] <= value <= interval_1[1]
        or interval_2[0] <= value <= interval_2[1]
    )


def permute(field_names: list, path: list, field_id: int):
    # stop recursion: we have found a working permutation
    if not field_names:
        return path
    # try all valid permutations
    for i, name in enumerate(field_names):
        if name in ticket_fields[field_id]:
            # backtrack
            result = permute(
                field_names[:i] + field_names[i + 1 :],
                path + [field_names[i]],
                field_id + 1,
            )
            # pass through result to first function call
            if result is not None:
                return result
    return None


if __name__ == "__main__":
    with open("input.txt") as file:
        lines = file.read()

    ticket_fields, own_ticket, nearby_tickets = [
        x.splitlines() for x in lines.split("\n\n")
    ]

    # parse own ticket
    own_ticket.pop(0)
    own_ticket = [int(value) for value in own_ticket[0].split(",")]
    # parse nearby tickets
    nearby_tickets.pop(0)
    nearby_tickets = [
        [int(num) for num in ticket.split(",")] for ticket in nearby_tickets
    ]

    # parse ticket field rules
    field_rules = {}
    for ticket_rule in ticket_fields:
        re_groups = re.match(
            "([a-z]+(?: [a-z]+)*): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)", ticket_rule
        ).groups()
        field_name = re_groups[0]
        first_range = (int(re_groups[1]), int(re_groups[2]))
        second_range = (int(re_groups[3]), int(re_groups[4]))
        field_rules[field_name] = (first_range, second_range)

    # Find invalid values in tickets and only keep valid tickets
    invalid_values = []
    valid_tickets = []
    for ticket in nearby_tickets:
        is_ticket_valid = True
        for value in ticket:
            is_value_valid = False
            for intervals in field_rules.values():
                if is_valid_value(value, intervals):
                    is_value_valid = True
                    break
            if not is_value_valid:
                is_ticket_valid = False
                invalid_values.append(value)
        if is_ticket_valid:
            valid_tickets.append(ticket)

    print("Part 1:", sum(invalid_values))

    # create dict mapping a field_id to it's possible field_names
    ticket_fields = {}
    ticket_field_count = len(nearby_tickets[0])
    for i in range(ticket_field_count):
        ticket_fields[i] = set(field_rules.keys())

    for ticket in valid_tickets:
        for field_id, value in enumerate(ticket):
            for field_name in field_rules.keys():
                if not is_valid_value(value, field_rules[field_name]):
                    ticket_fields[field_id].remove(field_name)

    # find the matching order of field names
    field_names = list(field_rules.keys())
    fields = permute(field_names, [], 0)
    ordered_ticket_fields = {
        field_name: field_id for field_id, field_name in enumerate(fields)
    }

    # get result for part 2
    result = 1
    for field_name, field_id in ordered_ticket_fields.items():
        if field_name.startswith("departure"):
            result *= own_ticket[field_id]

    print("Part 2:", result)
