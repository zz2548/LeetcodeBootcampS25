class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        '''
        # Naive
        stack = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    stack.append((i, j))
        while stack:
            row, col = stack.pop()
            for i in range(len(matrix[0])):
                matrix[row][i] = 0
            for i in range(len(matrix)):
                matrix[i][col] = 0
        '''

        if not matrix:
            return []

        m = len(matrix)
        n = len(matrix[0])

        # Using first row/col to store whether or not we have a zero on that row/col
        # Separately keep track of it's original value
        first_row_has_zero = False
        first_col_has_zero = False

        # Mark the rows/cols for change
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    if row == 0:
                        first_row_has_zero = True
                    if col == 0:
                        first_col_has_zero = True
                    matrix[row][0] = matrix[0][col] = 0
                    # Change the values based on first num
        for row in range(1, m):
            for col in range(1, n):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0
        # Update first rows/cols
        if first_row_has_zero:
            for col in range(n):
                matrix[0][col] = 0
        if first_col_has_zero:
            for row in range(m):
                matrix[row][0] = 0

        # Runtime O(m * n), Space O(1)