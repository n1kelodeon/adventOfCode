from bag import Bag

with open("input.txt", "r") as file:
    lines = file.read().splitlines()


def create_bag_tree(use_single_bags: bool) -> dict:
    bags = {}
    for line in lines:
        line = line.split(" bags contain ")
        parent_color = line[0]
        parent_bag = bags.get(parent_color)
        # add bag definition if not in bags dict yet
        if parent_bag is None:
            parent_bag = Bag(color=parent_color)
            bags.update({parent_color: parent_bag})
        if line[1] != "no other bags.":
            child_bags = line[1].split(", ")
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
