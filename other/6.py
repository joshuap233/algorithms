# 座标从（1，1） 开始

from typing import List

n, m = map(int, input().split())

maps = []
for _ in range(n):
    a = input()
    maps.append(a)

k = int(input())

a = []
for _ in range(k):
    a = list(map(lambda x: int(x) - 1, input().split()))
    maps.append(a)


def main(nums: List[str], army: List[List[int]]):
    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            if nums[i][j] == '1':
                dp[i][j] = float('inf')
