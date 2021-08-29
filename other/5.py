# coding=utf-8
# 本题为考试单行多行输入输出规范示例，无需提交，不计分。
import math


# n, k = map(int, input().split())
# a = list(map(int, input().split()))


def main(nums: list, cnt: int):
    maxi = max(nums)
    for i in nums:
        cnt -= maxi - i
        if cnt <= 0:
            return maxi
    return maxi + math.ceil(cnt / len(nums))


print(main([1, 1, 1], 1))
