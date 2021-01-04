#%%
import re

if __name__ == "__main__":
    with open("16/input.txt") as file:
        lines = file.read()

    ticket_fields, own_ticket, nearby_tickets = [
        x.splitlines() for x in lines.split("\n\n")
    ]

ticket_rules = {}
for ticket_rule in ticket_fields:
    re_groups = re.match(
        "([a-z]+(?: [a-z]+)*): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)", ticket_rule
    ).groups()
    field_name = re_groups[0]
    first_range = (int(re_groups[1]), int(re_groups[2]))
    second_range = (int(re_groups[3]), int(re_groups[4]))
    ticket_rules[field_name] = (first_range, second_range)

nearby_tickets.pop(0)
nearby_tickets = [[int(num) for num in ticket.split(",")] for ticket in nearby_tickets]

invalid_values = []
for ticket in nearby_tickets:
    for num in ticket:
        is_valid = False
        for first_range, second_range in ticket_rules.values():
            if (
                first_range[0] <= num <= first_range[1]
                or second_range[0] <= num <= second_range[1]
            ):
                is_valid = True
                break
        if not is_valid:
            invalid_values.append(num)

print("Part 1:", sum(invalid_values))
