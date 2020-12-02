from os import path

dir_path = path.dirname(path.realpath(__file__))

f = open(path.join(dir_path, "input.txt"), "r")
number_set = set(map(int, f.readlines()))


def find_pair_with_sum(sum):
    for number in number_set:
        complement = sum - number
        if complement in number_set:
            return (number, complement)
    return None


# pt. 1
(a, b) = find_pair_with_sum(2020)
print(a * b)

# pt. 2
for number in number_set:
    pair = find_pair_with_sum(2020 - number)
    if pair is not None:
        print(pair[0] * pair[1] * number)
        exit(0)
