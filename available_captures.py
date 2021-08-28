from typing import List


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        def find_rook():
            for i, row in enumerate(board):
                for j, square in enumerate(row):
                    if square == "R":
                        return i, j

        x, y = find_rook()

        def check_right():
            for i in range(y + 1, len(board[x])):
                if board[x][i] == "B":
                    break
                elif board[x][i] == "p":
                    return 1
            return 0

        def check_left():
            for i in reversed(range(0, y)):
                if board[x][i] == "B":
                    break
                elif board[x][i] == "p":
                    return 1
            return 0

        def check_up():
            for i in reversed(range(0, x)):
                if board[i][y] == "B":
                    break
                elif board[i][y] == "p":
                    return 1
            return 0

        def check_down():
            for i in range(x + 1, len(board)):
                if board[i][y] == "B":
                    break
                elif board[i][y] == "p":
                    return 1
            return 0

        return check_up() + check_right() + check_down() + check_left()


sol = Solution()
assert sol.numRookCaptures([[".", ".", ".", ".", ".", ".", ".", "."], [".", "p", "p", "p", "p", "p", ".", "."],
                            [".", "p", "p", "B", "p", "p", ".", "."], [".", "p", "B", "R", "B", "p", ".", "."],
                            [".", "p", "p", "B", "p", "p", ".", "."], [".", "p", "p", "p", "p", "p", ".", "."],
                            [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]) == 0
assert sol.numRookCaptures([[".", ".", ".", ".", ".", ".", ".", "."], [".", ".", "B", "B", "B", "B", "B", "."],
                            [".", "p", "B", "p", "p", "p", "B", "p"], [".", "p", "B", "p", "R", "p", "B", "p"],
                            [".", "p", "B", "p", "p", "p", "B", "p"], [".", ".", "B", "B", "B", "B", "B", "."],
                            [".", ".", ".", "p", "p", "p", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]) == 4
