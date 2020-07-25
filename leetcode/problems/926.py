# 926. 将字符串翻转到单调递增
# https://leetcode-cn.com/problems/flip-string-to-monotone-increasing/

# 超出时间限制
class Solution:
    def minFlipsMonoIncr(self, string: str) -> int:
        zero = set([])
        one = set([])
        min_ = float('inf')
        start = None
        for index, item in enumerate(string):
            if item == '1':
                start = index
                break
        if start is None:
            return 0
        for index, item in enumerate(string[start:]):
            true_index = index + start
            if item == '0':
                zero.add(true_index)
            else:
                one.add(true_index)
        # 从start开始翻,index之前置0,之后置1
        for index in range(start, len(string)):
            count = 0
            for i in zero:
                if i > index:
                    count += 1
            for i in one:
                if i < index:
                    count += 1
            min_ = min(min_, count)
        return min_


# 76ms, O(n)
class Solution2:
    def minFlipsMonoIncr(self, string: str) -> int:
        start = self.get_start(string)
        if start is None:
            return 0
        rightZeroCount = self.get_zero_count(string[start:])
        leftOneCount = 0
        min_ = float('inf')
        for item in string[start:]:
            # 计算出左边1的个数,右边0的个数
            min_ = min(min_, leftOneCount + rightZeroCount)
            if item == '1':
                leftOneCount += 1
            else:
                rightZeroCount -= 1
        min_ = min(min_, leftOneCount + rightZeroCount)
        return min_

    @staticmethod
    def get_start(string) -> int:
        start = None
        for index, item in enumerate(string):
            if item == '1':
                start = index
                break
        return start

    @staticmethod
    def get_zero_count(string):
        zero = 0
        for item in string:
            if item == '0':
                zero += 1
        return zero


s = Solution2()
print(s.minFlipsMonoIncr('00011000'))
