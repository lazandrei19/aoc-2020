from os import path
import re

dir_path = path.dirname(path.realpath(__file__))

f = open(path.join(dir_path, "input.txt"), "r")

input_format = re.compile(r'^(\d+)-(\d+) (.): (.*)$')


def split_input(input_line):
    matches = re.match(input_format, input_line)
    (minS, maxS, char, string) = matches.group(1, 2, 3, 4)
    return (int(minS), int(maxS), char, string)


def check_input1(min_count, max_count, char, string):
    char_count = {}
    for c in range(ord('a'), ord('z') + 1):
        char_count[chr(c)] = 0
    for c in string:
        char_count[c] += 1
    return min_count <= char_count[char] <= max_count


def check_input2(pos1, pos2, char, string):
    return (string[pos1 - 1] == char) != (string[pos2 - 1] == char)


input_lines = list(map(split_input, f.readlines()))
valid_passwords1 = filter(lambda x: check_input1(x[0], x[1], x[2],
                                                 x[3]), input_lines)

# pt. 1
print(len(list(valid_passwords1)))


valid_passwords2 = filter(lambda x: check_input2(x[0], x[1], x[2],
                                                 x[3]), input_lines)

# pt. 2
print(len(list(valid_passwords2)))
