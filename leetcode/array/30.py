class Solution:
    def isValidSudoku(self, board) -> bool:
        if self.column_has_repeat(board):
            return False
        if self.row_has_repeat(board):
            return False
        if self.sudoku9_has_repeat(board):
            return False
        return True

    @staticmethod
    def has_repeat_number(array: list):
        newList = list(filter(lambda item: item != '.', array))
        return len(set(newList)) != len(newList)

    def row_has_repeat(self, board):
        # 遍历行
        for item in board:
            if self.has_repeat_number(item):
                return True
        return False

    def column_has_repeat(self, board):
        # 遍历列
        x = 0
        while x < 9:
            temp = []
            y = 0
            while y < 9:
                temp.append(board[y][x])
                y += 1
            if self.has_repeat_number(temp):
                return True
            x += 1
            temp.clear()
        return False

    def sudoku9_has_repeat(self, board):
        # 遍历3x3格
        x = 0
        y = 0
        startY = y
        temp = []
        while y < 9:
            temp.extend(board[y][x:x + 3])
            temp.extend(board[y + 1][x:x + 3])
            temp.extend(board[y + 2][x:x + 3])
            x += 3

            if self.has_repeat_number(temp):
                return True
            temp.clear()
            if x == 9:
                x = 0
                startY += 3

            y = startY
        return False


s = Solution()
res = s.isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."],
                       ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                       [".", "9", "8", ".", ".", ".", ".", "6", "."],
                       ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                       ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                       ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                       [".", "6", ".", ".", ".", ".", "2", "8", "."],
                       [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                       [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
                      )
print(res)
