# 旋转图像


class Solution:
    def rotate(self, matrix) -> None:
        """
            [x][y] -> [n-y-1][x]
            [x][y] -> [n-y-1][x]

            matrix[y][x]
        """
        n = len(matrix)
        layer = n
        start = 0

        # 分层交换:
        while layer > 0:
            x, y = (start, start)
            for _ in range(layer - 1):
                temp = [matrix[y][x]]
                # 每次交换四个
                for _ in range(4):
                    temp.append(matrix[x][n - y - 1])
                    matrix[x][n - y - 1] = temp.pop(0)
                    x, y = n - y - 1, x
                x += 1
            layer -= 2
            start += 1


matrix = [
    [2, 29, 20, 26, 16, 28],
    [12, 27, 9, 25, 13, 21],
    [32, 33, 32, 2, 28, 14],
    [13, 14, 32, 27, 22, 26],
    [33, 1, 20, 7, 21, 7],
    [4, 24, 1, 6, 32, 34]
]

s = Solution()
s.rotate(matrix)
print(matrix)
