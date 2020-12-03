
def readFile() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        return [line[:-1] for line in f.readlines()]

def count_trees(mylist, dx, dy):
    x, y, cnt, length, mod = 0, 0, 0, len(mylist) - dy, len(mylist[0])
    while y < length:
        x = (x + dx) % mod
        y += dy
        if mylist[y][x]  == '#':
            cnt += 1
    return cnt

def part1(mylist):
    return count_trees(mylist, 3, 1)

def part2(mylist, part1sol):
    slopes = ((1,1), (5,1), (7,1), (1,2))
    prod = part1sol
    for slope in slopes:
        prod *= count_trees(mylist, slope[0], slope[1])
    return prod
def test():
    test_input = [
    "..##.........##.........##.........##.........##.........##.......",
    "#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..",
    ".#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.",
    "..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#",
    ".#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.",
    "..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....",
    ".#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#",
    ".#........#.#........#.#........#.#........#.#........#.#........#",
    "#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...",
    "#...##....##...##....##...##....##...##....##...##....##...##....#",
    ".#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#",
    ]

    assert part1(test_input) == 7
    assert part2(test_input, 7) == 336

test()
mylist = readFile()
print(f'Part 1 {part1(mylist)}')
print(f'Part 2 {part2(mylist, 220)}')
