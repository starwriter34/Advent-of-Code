#### `##################################`
#### `--- Day 3: Toboggan Trajectory ---`
#### `###################################`

#### `####################`
#### `------ Part 1 ------`
#### `####################`

[Day 3](https://adventofcode.com/2020/day/3)

With the toboggan login problems resolved, you set off toward the airport.<br>While travel by toboggan might be easy, it's certainly not safe: there's<br>very minimal steering and the area is covered in trees. You'll need to see<br>which angles will take you near the fewest trees.<br>

Due to the local geology, trees in this area only grow on exact integer<br>coordinates in a grid. You make a map (your puzzle input) of the open<br>squares (.) and trees (#) you can see. For example:<br>

..##.......<br>
#...#...#..<br>
.#....#..#.<br>
..#.#...#.#<br>
.#...##..#.<br>
..#.##.....<br>
.#.#.#....#<br>
.#........#<br>
#.##...#...<br>
#...##....#<br>
.#..#...#.#<br>

These aren't the only trees, though; due to something you read about once<br>involving arboreal genetics and biome stability, the same pattern repeats<br>to the right many times:<br>

..##.........##.........##.........##.........##.........##.......  ---><br>
#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..<br>
.#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.<br>
..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#<br>
.#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.<br>
..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....  ---><br>
.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#<br>
.#........#.#........#.#........#.#........#.#........#.#........#<br>
#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...<br>
#...##....##...##....##...##....##...##....##...##....##...##....#<br>
.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#  ---><br>

You start on the open square (.) in the top-left corner and need to reach<br>the bottom (below the bottom-most row on your map).<br>

The toboggan can only follow a few specific slopes (you opted for a cheaper<br>model that prefers rational numbers); start by **counting all the trees** you<br>would encounter for the slope **right 3, down 1:**<br>

From your starting position at the top-left, check the position that is<br>right 3 and down 1. Then, check the position that is right 3 and down 1<br>from there, and so on until you go past the bottom of the map.<br>

The locations you'd check in the above example are marked here with **O** where<br>there was an open square and X where there was a tree:<br>

..##.........##.........##.........##.........##.........##.......  ---><br>
#..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..<br>
.#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.<br>
..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#<br>
.#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.<br>
..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  ---><br>
.#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#<br>
.#........#.#........X.#........#.#........#.#........#.#........#<br>
#.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...<br>
#...##....##...##....##...#X....##...##....##...##....##...##....#<br>
.#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  ---><br>

In this example, traversing the map using this slope would cause you to<br>encounter 7 trees.<br>

Starting at the top-left corner of your map and following a slope of<br>right 3 and down 1, **how many trees would you encounter?**<br>

#### `####################`
#### `------ Part 2 ------`
#### `####################`

Time to check the rest of the slopes - you need to minimize the probability<br>of a sudden arboreal stop, after all.<br>

Determine the number of trees you would encounter if, for each of the<br>following slopes, you start at the top-left corner and traverse the map all<br>the way to the bottom:<br>

Right 1, down 1.<br>
Right 3, down 1. (This is the slope you already checked.)<br>
Right 5, down 1.<br>
Right 7, down 1.<br>
Right 1, down 2.<br>
In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s)<br>respectively; multiplied together, these produce the answer **336**.<br>

**What do you get if you multiply together the number of trees encountered on<br>each of the listed slopes?**