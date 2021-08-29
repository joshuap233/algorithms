# https://leetcode-cn.com/problems/rabbits-in-forest/
# 781. 森林中的兔子


from typing import List
from collections import Counter
import math


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counter = Counter(answers)
        cnt = 0
        for v, c in counter.items():
            cnt += math.ceil(c / (v + 1)) * (v + 1)
        return cnt
