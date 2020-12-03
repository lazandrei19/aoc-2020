from os import path
import re

dir_path = path.dirname(path.realpath(__file__))

f = open(path.join(dir_path, "input.txt"), "r")


def transform_input(input_line: str):
    return list(map(lambda x: True if x == '#' else False, input_line.rstrip()))


input = list(map(transform_input, f.readlines()))
w = len(input[0])
h = len(input)


def count_trees(dx, dy):
    count = 0

    for i in range(1, int(h / dy)):
        if input[i * dy][i * dx % w]:
            count += 1

    return count


# pt. 1
print(count_trees(3, 1))

# pt. 2

slope1 = count_trees(1, 1)
slope2 = count_trees(3, 1)
slope3 = count_trees(5, 1)
slope4 = count_trees(7, 1)
slope5 = count_trees(1, 2)

print(slope1 * slope2 * slope3 * slope4 * slope5)
