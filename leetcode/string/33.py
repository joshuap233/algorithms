# 整数反转


class Solution:
    def reverse(self, x: int) -> int:
        minus = True if x < 0 else False
        x = abs(x)
        array = list(str(x))
        for i in range(len(array) // 2):
            array[i], array[-(i + 1)] = array[-(i + 1)], array[i]

        index = 0
        while True:
            if len(array) == 0 or array[index] != '0':
                break
            if array[index] == '0':
                array.pop(index)

        number = 0
        for index, value in enumerate(reversed(array)):
            number += (10 ** index) * int(value)
        if minus:
            number = -number
            if number < -2 ** 31:
                return 0
        if number > 2 ** 31 - 1:
            return 0
        return number


s = Solution()
s.reverse(1563847412)
