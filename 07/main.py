from bag import Bag


def create_bag_tree(bag_rules: [str], use_single_bags: bool) -> dict[str, Bag]:
    bags = {}
    for rule in bag_rules:
        rule = rule.split(" bags contain ")
        parent_color = rule[0]
        parent_bag = bags.get(parent_color)
        # add bag definition if not in bags dict yet
        if parent_bag is None:
            parent_bag = Bag(color=parent_color)
            bags.update({parent_color: parent_bag})
        if rule[1] != "no other bags.":
            child_bags = rule[1].split(", ")
            for child_bag in child_bags:
                child_bag = child_bag.split(" bag")[0]
                amount, child_color = child_bag.split(" ", 1)
                child_bag = bags.get(child_color)
                # add bag definition if not in bags dict yet
                if child_bag is None:
                    child_bag = Bag(color=child_color)
                    bags.update({child_color: child_bag})
                if use_single_bags:
                    amount = 1
                parent_bag.add_child(child_bag, int(amount))
    return bags


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        bag_rules = file.read().splitlines()

    bags_1 = create_bag_tree(bag_rules, use_single_bags=True)
    shiny_gold_count = 0
    for bag in bags_1.values():
        if bag.count_shiny_gold_bags() > 0:
            shiny_gold_count += 1
    print("Part 1", shiny_gold_count)

    bags_2 = create_bag_tree(bag_rules, use_single_bags=False)
    shiny_gold_bag = bags_2["shiny gold"]
    print("Part 2", shiny_gold_bag.count_bags())
