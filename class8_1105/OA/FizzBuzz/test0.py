"""
Given a number n, for each integer i in the range from 1 to n inclusive,
print one value per line as follows:

    if i is a multple of both 3 and 5, print FizzBuzz.
    if i is a multiple of 3 (but not 5), print Fizz.
    if i is a multiple of 5 (but not 3), print Buzz.
    if i is not a multiple of 3 or 5, print the value of i.

parameter(s):
    int(n): upper limit of values to test (inclusive)
returns:
    None
prints:
    the function must print the appropriate response for each value i in the set {1,2,3 ... ,n} in ascending order,
    each on a separate line.

Constraints

    0 < n < 2 * 10^5

Sample Output
    1
    2
    Fizz
    4
    Buzz
    Fizz
    7
    8
    Fizz
    Buzz
    11
    Fizz
    13
    14
    FizzBuzz
"""

def FizzBuzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


if __name__ == '__main__':
    n = int(input("Enter n: "))
    FizzBuzz(n)
