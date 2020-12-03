
#### `##################################`
#### `--- Day 2: Password Philosophy ---`
#### `###################################`

#### `####################`
#### `------ Part 1 ------`
#### `####################`

[Day 2](https://adventofcode.com/2020/day/2)

Your flight departs in a few days from the coastal airport; the easiest way<br>
down to the coast from here is via toboggan.

The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day.<br>
"Something's wrong with our computers; we can't log in!" You ask if you can<br>
take a look.<br>

Their password database seems to be a little corrupted: some of the<br>
passwords wouldn't have been allowed by the Official Toboggan Corporate<br>
Policy that was in effect when they were chosen.<br>

To try to debug the problem, they have created a list (your puzzle input)<br>
of **passwords** (according to the corrupted database) and **the corporate policy**<br>
**when that password was set**.

For example, suppose you have the following list:<br>

    1-3 a: abcde
    1-3 b: cdefg
    2-9 c: ccccccccc

Each line gives the password policy and then the password. The password<br>
policy indicates the lowest and highest number of times a given letter must<br>
appear for the password to be valid. For example, 1-3 a means that the<br>
password must contain a at least 1 time and at most 3 times.<br>

In the above example, 2 passwords are valid. The middle password, cdefg, is<br>
not; it contains no instances of b, but needs at least 1. The first and<br>
third passwords are valid: they contain one a or nine c, both within the<br>
limits of their respective policies.<br>

**How many passwords are valid** according to their policies?<br>

#### `####################`
#### `------ Part 2 ------`
#### `####################`

While it appears you validated the passwords correctly, they don't seem to<br>
be what the Official Toboggan Corporate Authentication System is expecting.<br>

The shopkeeper suddenly realizes that he just accidentally explained the<br>
password policy rules from his old job at the sled rental place down the<br>
street! The Official Toboggan Corporate Policy actually works a little<br>
differently.<br>

Each policy actually describes two **positions in the password**, where 1 means<br>
the first character, 2 means the second character, and so on. (Be careful;<br>
Toboggan Corporate Policies have no concept of "index zero"!) **Exactly one of**<br>
**these positions** must contain the given letter. Other occurrences of the<br>
letter are irrelevant for the purposes of policy enforcement.<br>

Given the same example list from above:<br>

<code>1-3 a: <b>a</b>b<b>c</b>de is <b>valid</b>: position 1 contains a and position 3 does not.
1-3 b: <b>c</b>d<b>e</b>fg is <b>invalid</b>: neither position 1 nor position 3 contains b.
2-9 c: c<b>c</b>*cccccc<b>c</b> is <b>invalid</b>: both position 2 and position 9 contain c.</code>

**How many passwords are valid** according to the new interpretation of the policies?