# 外观数列

class Solution:
    def countAndSay(self, n: int) -> str:
        pre = '1'
        for i in range(n - 1):
            pre = self.get_sequence(pre)
        return pre

    def get_sequence(self, value: str) -> str:
        res = ''
        count = 1
        for index, item in enumerate(value):
            if self.has_next(value, index):
                next_ = value[index + 1]

                if item == next_:
                    count += 1
                else:
                    res = res + str(count) + value[index]
                    count = 1
            else:
                return res + str(count) + item

    @staticmethod
    def has_next(array, index):
        return True if index + 1 < len(array) else False


s = Solution()
print(s.countAndSay(5))
