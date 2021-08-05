# https://leetcode-cn.com/problems/task-scheduler/
# 621. 任务调度器

from typing import List


class Solution:
    """
        完成所有任务的最短时间取决于出现次数最多的任务数量。

        比如 a -- a -- a -- ....
        -- 为时间间隔
        因此我们只需要在间隔之间插空即可

        如果空位都插满之后还有任务，那就随便在这些间隔里面插入就可以，
        因为间隔长度肯定会大于n，在这种情况下就是任务的总数是最小所需时间

    """

    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter
        c = [v for i, v in Counter(tasks).most_common()]
        # 至少需要的时间
        res = c[0] + (c[0] - 1) * n


s = Solution()
s.leastInterval(["A", "A", "A", "B", "B", "B", "B"], 2)
