from collections import deque


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        row = len(matrix)
        col = len(matrix[0])
        direction = 'right'

        cur_row = 0
        cur_col = 0
        total = 0
        q = deque()
        visited = set()
        result = []

        while total < row * col:
            if (cur_row, cur_col) not in visited:
                # result.append(matrix[cur_row][cur_col])
                q.append(matrix[cur_row][cur_col])
                visited.add((cur_row, cur_col))
                total += 1
            if direction == 'right':
                if cur_col < col and cur_col + 1 < col:
                    # check index not out of range
                    if (cur_row, cur_col + 1) not in visited:
                        cur_col += 1
                    else:
                        direction = 'down'
                else:
                    direction = 'down'
            elif direction == 'down':
                if cur_row < row and cur_row + 1 < row:
                    if (cur_row + 1, cur_col) not in visited:
                        cur_row += 1
                    else:
                        direction = 'left'
                else:
                    direction = 'left'
            elif direction == 'left':
                if cur_col > -1 and cur_col - 1 > -1:
                    # check index not out of range
                    if (cur_row, cur_col - 1) not in visited:
                        cur_col -= 1
                    else:
                        direction = 'up'
                else:
                    direction = 'up'
            elif direction == 'up':
                if cur_row > -1 and cur_row - 1 > -1:
                    if (cur_row - 1, cur_col) not in visited:
                        cur_row -= 1
                    else:
                        direction = 'right'
                else:
                    direction = 'right'

        while len(q) != 0:
            result.append(q.popleft())

        return result


if __name__ == '__main__':
    obj = Solution()

    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    res = obj.spiralOrder(matrix)
    # res = obj.calculate(s)
    #
    print(res)
