from os import path

dir_path = path.dirname(path.realpath(__file__))

f = open(path.join(dir_path, "input.txt"), "r")
passes = f.readlines()


def high_low(c):
    if c == 'F' or c == 'L':
        return '0'
    return '1'


def convert_to_id(pass_dir: str):
    bin_str = ''.join(list(map(high_low, pass_dir.strip())))
    return int(bin_str, 2)


ids = list(map(convert_to_id, passes))
ids.sort()


# Pt. 1
print(ids[-1])

for i in range(len(ids)):
    if ids[i] + 2 == ids[i+1]:
        print(ids[i] + 1)
        exit(0)
