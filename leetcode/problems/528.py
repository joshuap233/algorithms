from typing import List
from itertools import accumulate
import random
from bisect import bisect_left


class Solution:

    def __init__(self, w: List[int]):
        self.nums = list(accumulate(w))
        self.s = self.nums[-1]

    def pickIndex(self) -> int:
        x = random.randint(1, self.s)
        return bisect_left(self.nums, x)
