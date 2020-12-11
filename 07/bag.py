class Bag:
    def __init__(self, color):
        self.color = color
        self.child_bags = []
        self.has_shiny_bag = False

    def add_child(self, bag, amount):
        for i in range(amount):
            self.child_bags.append(bag)

    def count_shiny_gold_bags(self):
        count = 0
        for child_bag in self.child_bags:
            if child_bag.color == "shiny gold":
                count += 1
            count += child_bag.count_shiny_gold_bags()
        return count

    def count_bags(self):
        count = 0
        for child_bag in self.child_bags:
            count += 1
            count += child_bag.count_bags()
        return count
