class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        # submit accept

        cols = set()
        up_hill = set()
        down_hill = set()

        res = []
        curr_puzzle = [["."] * n for i in range(n)]

        def helper(row_idx):
            if row_idx == n:
                copy = [''.join(row) for row in curr_puzzle]
                res.append(copy)
                return

            for col_idx in range(n):
                if col_idx in cols or (row_idx + col_idx) in up_hill or (row_idx - col_idx) in down_hill:
                    continue
                curr_puzzle[row_idx][col_idx] = "Q"
                cols.add(col_idx)
                up_hill.add(row_idx + col_idx)
                down_hill.add(row_idx - col_idx)

                helper(row_idx + 1)

                curr_puzzle[row_idx][col_idx] = "."
                cols.remove(col_idx)
                up_hill.remove(row_idx + col_idx)
                down_hill.remove(row_idx - col_idx)

        helper(0)
        return len(res)