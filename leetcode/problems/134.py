# https://leetcode-cn.com/problems/gas-station/
# 134. 加油站
from typing import List


class Solution:
    """
        如果题目有解，该答案即为唯一答案。
        如果从 0 开始, 到达 k 站后,没油了,那么从 k 开始重新计数,

        可以不将 0-k 之间的站作为起点, 0-k 站, 剩余油量必定 >=0,
        而从 0-站之间开始计数, 那么初始油量 = 0(不计算当前站可加油量)


    """

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        total = rest = 0

        for i in range(len(gas)):
            rest += gas[i] - cost[i]
            total += gas[i] - cost[i]
            if rest < 0:
                start = i + 1
                rest = 0

