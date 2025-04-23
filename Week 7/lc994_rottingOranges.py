class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        mins = 0
        freshCount = 0
        rotten = collections.deque()
        rows = len(grid)
        cols = len(grid[0])

        # Traverse through the grid
        for i in range(rows):
            for j in range(cols):
                # If fresh, add to fresh count
                if grid[i][j] == 1:
                    freshCount += 1
                # If rotten, add to the rotten queue
                if grid[i][j] == 2:
                    rotten.append((i, j))
        # While we have rotten oranges
        while rotten and freshCount > 0:
            mins += 1
            for _ in range(len(rotten)):
                [r, c] = rotten.popleft()

                for d in dir:
                    # Out of bound
                    if r + d[0] < 0 or r + d[0] == rows or c + d[1] < 0 or c + d[
                        1] == cols:
                        continue
                    # Rotten already or Empty
                    if grid[r + d[0]][c + d[1]] == 0 or grid[r + d[0]][c + d[1]] == 2:
                        continue
                    # Fresh -> Rotten
                    freshCount -= 1
                    grid[r + d[0]][c + d[1]] = 2
                    rotten.append((r + d[0], c + d[1]))
        return mins if freshCount == 0 else -1


