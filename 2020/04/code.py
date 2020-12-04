import re

def readFile(file):
    with open(file) as f:
        rawdata = []
        s = ''
        for d in f.read().splitlines():
            if d == '':
                rawdata.append(s)
                s = ''
            else:
                s += d + ' '
        rawdata.append(s)
    return [dict([tuple(l.split(':')) for l in d.split()]) for d in rawdata]

def validate(mylist):
    test = ['hcl', 'iyr', 'eyr', 'ecl', 'pid', 'byr', 'hgt']
    return all(k in mylist for k in test)

def validate_key(key, value):
    if key == 'byr':
        return value.isdigit() and 1920 <= int(value) <= 2002
    if key == 'iyr':
        return value.isdigit() and 2010 <= int(value) <= 2020
    if key == 'eyr':
        return value.isdigit() and 2020 <= int(value) <= 2030
    if key == 'hgt':
        n = value[:-2]
        if not n.isdigit():
            return False
        unit = value[-2:]
        if unit == 'cm':
            return 150 <= int(n) <= 193
        if unit == 'in':
            return 59 <= int(n) <= 76
        return False
    if key == 'hcl':
        return value[0] == '#' and re.fullmatch(r'[a-f\d]{6}', value[1:]) is not None
    if key == 'ecl':
        return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if key == 'pid':
        return value.isdigit() and len(value) == 9


def validate_keys(passport):
    keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for k in keys:
        if k not in passport or not validate_key(k, passport[k]):
            return False
    return True

def part1(mylist):
    return sum(map(validate, mylist))

def part2(data):
    return sum(map(validate_keys, data))

def test():
    test_input = [{'hcl':'#ae17e1', 'iyr':2013, 'eyr':2024, 'ecl':'brn', 'pid':760753108, 'byr':1931, 'hgt':'179cm'}]
    test_inputb = [['hcl', 'iyr', 'eyr', 'ecl', 'pid', 'byr', 'hgt'],]

    assert part1(test_input) == 1

test()
mylist = readFile(f"{__file__.rstrip('code.py')}input.txt")
print(f'Part 1 {part1(mylist)}')
print(f'Part 2 {part2(mylist)}')
