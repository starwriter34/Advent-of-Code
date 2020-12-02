import re

VOWEL = { "a": 1,"e": 1,"i": 1,"o": 1,"u": 1, }
DOUBLE = re.compile(r"(.)\1")
FORBIDDEN = re.compile(r"(ab|cd|pq|xy)")
ABA = re.compile(r"(.).\1")
DOUBLE_PAIR = re.compile(r"(..).*\1")
def readFile() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        return [str(line[:-1]) for line in f.readlines()]

def part1(mylist) -> bool:

    return bool(check_vowels(mylist)) and bool(has_double(mylist)) and not bool(has_forbidden(mylist))

def part2(mylist) -> bool:
    return bool(re.search(ABA, mylist)) and bool(re.search(DOUBLE_PAIR, mylist))

def check_vowels(mylist) -> bool:
    count = 0
    for a in mylist:
        if a in VOWEL:
            count += 1
        if count >= 3:
            return True
    return False

def has_double(mylist) -> bool:
    return bool(re.search(DOUBLE, mylist))

def has_forbidden(mylist) -> bool:
    """ Does the string contain one of the forbidden substrings "ab" "cd" "pq"
    "xy"? """
    return bool(re.search(FORBIDDEN, mylist))

def test():
    assert part1('ugknbfddgicrmopn') == True
    assert part1('jchzalrnumimnmhp') == False
    assert part1('haegwjzuvuyypxyu') == False
    assert part1('dvszwmarrgswjxmb') == False

    assert part2('qjhvhtzxzqqjkmpb') == True
    assert part2('xxyxx') == True
    assert part2('uurcxstgmygtbstg') == False
    assert part2('ieodomkazucvgmuy') == False

test()
mylist = readFile()
print(sum(1 for line in mylist if part1(line)))
print(sum(1 for line in mylist if part2(line)))