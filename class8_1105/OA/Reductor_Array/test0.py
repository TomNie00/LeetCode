"""
For two integer arrays, the comparator value is the total number of elements in the first array such that there exists
no integer in the second array with an absolute difference less than or equal to d. Find the comparator value.
For example there are two arrays a = [ 7, 5, 9], b = [ 13, 1, 4 ], and the integer d = 3.
The absolute difference of a[0] to b[0] = | 7 - 13 | = 6, b[1] = | 7 - 1 | = 6, and b[2] = | 7 - 4 | = 3, to recap,
the values are 6, 6, 3. In this case, the absolute difference with b[2] is equal to d = 3,
so this element does not meet the criterion. A similar analysis of a[1] = 5 yields absolute differences of 8, 4, 1
and of a[2] = 9 yields 4, 8, 5. The only element of a that has an absolute difference with each element of b
that is always greater than d is element a[2], thus the comparator value is 1.


Function Description
Complete the function comparatorValue in the editor below.
The function must return an integer that denotes the comparator value of the arrays.

comparatorValue has the following parameter(s):
    a[a[0],...a[n − 1]]: an array of integers
    b[b[0],...b[m − 1]]: an array of integers
    d: an integer

Constraints
    1 ≤ n, m ≤ 10
    0 ≤ a[i], b[j], d ≤ 10

Sample Input For Custom Testing
    3
    3
    1
    5
    3
    5
    6
    7
    2

Sample Output
    1

Explanation
The first array a = [3, 1, 5] , the second array b = [5, 6, 7] ,
and d = 2 . Now find the absolute difference of each element of the first array with the elements of the second array:

For a[0] = 3, the differences are a[0] − b[0] = 3 − 5 = −2, a[0] − b[1] = 3 − 6 = −3,
and a[0] − b[2] = 3 − 7 = −4. Therefore, the absolute differences are [2, 3, 4]. For a[0] = 3,
there exists at least one integer in the second array with absolute difference less than or equal to d = 2.

For a[1] = 1, the differences are a[1] − b[0] = 1 − 5 = −4, a[1] − b[1] = 1 − 6 = −5,
and a[1] − b[2] = 1 − 7 = −6. Therefore, the absolute differences are [4, 5, 6]. For a[1] = 1,
there exists no integer in the second array with absolute difference less than or equal to d = 2.

For a[2] = 5, the differences are a[2] − b[0] = 5 − 5 = 0, a[2] − b[1] = 5 − 6 = −1,
and a[2] − b[2] = 5 − 7 = −2. Therefore, the absolute differences are [0, 1, 2]. For a[2] = 5,
there exists at least one integer in the second array with absolute difference less than or equal to d = 2.

The comparator value is 1.

"""


#
# Complete the 'comparatorValue' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
# 1. INTEGER_ARRAY a
# 2. INTEGER_ARRAY b
# 3. INTEGER d
#

def comparatorValue(a, b, d):
    comparator = 0

    for i in range(len(a)):
        go_next_index = False
        for y in range(len(b)):
            if abs(a[i] - b[y]) <= d:
                go_next_index = True
                break
        if not go_next_index:
            comparator += 1

    return comparator


if __name__ == '__main__':
    # arr_a = [3, 5, 9]
    # arr_b = [13, 1, 4]
    # d = 3

    arr_a = [3, 1, 5]
    arr_b = [7, 6, 5]
    d = 2

    print(comparatorValue(arr_a, arr_b, d))
