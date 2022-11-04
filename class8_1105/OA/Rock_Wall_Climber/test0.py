"""
A climber is trying to reach a flag that is some height above the ground. In the attempt to reach the flag,
the climber can make any number of jumps up the rock wall where the flag is mounted.
Movements can only be made up the wall, and the climber must end at exactly the height of the flag.

There are 2 types of jumps:

    1. A jump of height 1.
    2. A jump of height bigJump.

Determine the minimum number of jumps it will take the climber to reach the flag's exact height.


Example
    flagHeight = 8
    bigJump = 3

The climber starts at height 0,
takes two jumps of height bigJump and two of height 1 to reach exactly 8 units in 4 jumps.


Complete the function jumps in the editor below.
    jumps has the following parameter(s):
        int flagHeight: an integer, the flag height
        int bigJump: an integer, the height of the second type of jump

Returns:
    int: an integer, the minimum number of jumps necessary

Constraints
    1 ≤ bigJump, flagHeight ≤ 10

Input Format for Custom Testing
Input from stdin will be processed as follows and passed to the function.
    The first line contains an integer flagHeight.
    The second line contains an integer bigJump.

Sample Input
    STDIN Function
    ----- -----
    3 → flagHeight = 3
    1 → bigJump = 1

Sample Output
    3

Explanation
    The climber can only jump 1 unit or bigJump units. With bigJump = 1,
    the climber can only make 1-unit jumps. It will take 3 jumps to reach the flag.

"""


def climber(flagHeight, bigJump):
    res = 0
    while flagHeight:
        if flagHeight >= bigJump:
            flagHeight -= bigJump
            res += 1
        else:
            flagHeight -= 1
            res += 1
    return res


def best_climber(flagHeight, bigJump):
    if flagHeight % bigJump == 0:
        return flagHeight // bigJump
    else:
        return (flagHeight // bigJump) + (flagHeight % bigJump)


if __name__ == '__main__':
    flagHeight = int(input("Enter flagHeight: "))
    bigJump = int(input("Enter bigJump: "))
    print(best_climber(flagHeight, bigJump))
