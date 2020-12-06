from os import path

dir_path = path.dirname(path.realpath(__file__))

f = open(path.join(dir_path, "input.txt"), "r")

inputs = []
cur_input = ''
no_lines = 0
for line in f.readlines():
    cur_input += line.rstrip()
    no_lines += 1
    if line.rstrip() == '':
        inputs.append((cur_input, no_lines - 1))
        cur_input = ''
        no_lines = 0
inputs.append((cur_input, no_lines))


def check_input1(input):
    char_count = {}
    for c in range(ord('a'), ord('z') + 1):
        char_count[chr(c)] = 0
    for c in input:
        char_count[c] += 1
    return len(list(filter(lambda x: x > 0, char_count.values())))


# pt. 1
print(sum(map(lambda x: check_input1(x[0]), inputs)))


def check_input2(input, number_of_people):
    char_count = {}
    for c in range(ord('a'), ord('z') + 1):
        char_count[chr(c)] = 0
    for c in input:
        char_count[c] += 1
    return len(list(filter(lambda x: x == number_of_people, char_count.values())))


# pt. 2
print(sum(map(lambda x: check_input2(x[0], x[1]), inputs)))
