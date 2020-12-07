from os import path
import re

dir_path = path.dirname(path.realpath(__file__))

f = open(path.join(dir_path, "input.txt"), "r")

input_format = re.compile(
    r'^(\w+ \w+) bags contain (no other bags.|(\d+ \w+ \w+ bags?(, |.))+)$')

bags = {}
for line in f.readlines():
    matches = re.match(input_format, line.strip())
    (parent_bag, child_bags) = matches.group(1, 2)
    child_bags_type = child_bags.split(',')
    child_bags_type[-1] = child_bags_type[-1][:-1]
    [pb_pattern, pb_color] = parent_bag.split(' ')
    pb = (pb_pattern, pb_color)
    bags[pb] = []
    if child_bags_type[0] == 'no other bags':
        continue
    for child_bag in child_bags_type:
        [num, pattern, color, _] = child_bag.strip().split(' ')
        bags[pb].append((int(num), (pattern, color)))


parent_bags = [('shiny', 'gold')]
i = 0
while i < len(parent_bags):
    for bag in bags:
        for child_bag in bags[bag]:
            if child_bag[1] == parent_bags[i] and bag not in parent_bags:
                parent_bags.append(bag)
    i += 1

# pt. 1
print(len(parent_bags) - 1)


def count_all_child_bags(parent):
    if len(bags[parent]) == 0:
        return 0
    total_bags = 0
    for child_bag in bags[parent]:
        total_bags += child_bag[0] * (count_all_child_bags(child_bag[1]) + 1)
    return total_bags


# pt. 2
print(count_all_child_bags(('shiny', 'gold')))
