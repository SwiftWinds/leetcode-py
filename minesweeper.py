from typing import List


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        y, x = click
        height, width = len(board), len(board[0])
        if (y < 0 or y >= height) or (x < 0 or x >= width):
            return board

        def count_bombs():
            min_y = max(0, y - 1)
            max_y = min(height, y + 2)
            min_x = max(0, x - 1)
            max_x = min(width, x + 2)
            count = 0
            for i in range(min_y, max_y):
                for j in range(min_x, max_x):
                    if board[i][j] == "M":
                        count += 1
            return count

        if board[y][x] == "B" or board[y][x].isnumeric():
            return board
        if board[y][x] == "M":
            board[y][x] = "X"
            return board
        if board[y][x] == "E":
            num_bombs = count_bombs()
            if num_bombs > 0:
                board[y][x] = str(num_bombs)
            else:
                board[y][x] = "B"
                for i in range(y - 1, y + 2):
                    for j in range(x - 1, x + 2):
                        self.updateBoard(board, [i, j])
        return board


s = Solution()
print(s.updateBoard(
    [["E", "E", "E", "E", "E"],
     ["E", "E", "M", "E", "E"],
     ["E", "E", "E", "E", "E"],
     ["E", "E", "E", "E", "E"]], [3, 0]))
assert s.updateBoard(
    [["E", "E", "E", "E", "E"],
     ["E", "E", "M", "E", "E"],
     ["E", "E", "E", "E", "E"],
     ["E", "E", "E", "E", "E"]], [3, 0]) == \
       [["B", "1", "E", "1", "B"],
        ["B", "1", "M", "1", "B"],
        ["B", "1", "1", "1", "B"],
        ["B", "B", "B", "B", "B"]]
