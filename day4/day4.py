from os import path
import re

dir_path = path.dirname(path.realpath(__file__))

f = open(path.join(dir_path, "input.txt"), "r")

inputs = []
cur_input = ''
for line in f.readlines():
    cur_input += line.rstrip() + ' '
    if line.rstrip() == '':
        inputs.append(cur_input)
        cur_input = ''
inputs.append(cur_input)


def get_passport(input: str):
    passport = {}
    for pair in input.rstrip().split(' '):
        (key, value) = pair.split(':')
        passport[key] = value
    return passport


passports = map(get_passport, inputs)


def check_passport(passport, keys):
    for key in keys:
        if not key in passport:
            return False
    return True


valid_passports = list(filter(lambda p: check_passport(
    p, ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]), passports))

# Pt. 1
print(len(valid_passports))


# TODO: there is one invalid passport that passes this test
def check_passport_advanced(passport):
    byr = re.match(r"\d{4}", passport["byr"])
    if byr == None or int(byr.group(0)) < 1920 or int(byr.group(0)) > 2002:
        return False
    iyr = re.match(r"\d{4}", passport["iyr"])
    if iyr == None or int(iyr.group(0)) < 2010 or int(iyr.group(0)) > 2020:
        return False
    eyr = re.match(r"\d{4}", passport["eyr"])
    if eyr == None or int(eyr.group(0)) < 2020 or int(eyr.group(0)) > 2030:
        return False
    hgt = re.match(r"(\d+)(cm|in)", passport["hgt"])
    if hgt == None or (hgt.group(2) == "cm" and (int(hgt.group(1)) < 150
                                                 or int(hgt.group(1)) > 193)) or (hgt.group(2) == "in"
                                                                                  and (int(hgt.group(1)) < 59 or int(hgt.group(1)) > 76)):
        return False
    hcl = re.match(r"\#[0-9a-f]{6}", passport["hcl"])
    if hcl == None:
        return False
    if not passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False
    pid = re.match(r"\d{9}", passport["pid"])
    if pid == None:
        return False
    return True


valid_passports_advanced = filter(check_passport_advanced, valid_passports)

# Pt. 2
print(len(list(valid_passports_advanced)))
