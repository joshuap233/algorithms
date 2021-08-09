# https://leetcode-cn.com/problems/task-scheduler/
# 621. 任务调度器

from typing import List


class Solution:
    """
        模拟法:
        任务选择: 选择不在冷却中的剩余次数最多的任务
        慢的离谱....
        首先 选择冷却时间最小,且次数不为0的元素 a,a 的时间大于当前时间,
        则 times += a.time
        否则找到已经冷却的,次数最大的那个
        时间复杂度: O(len(task)* 任务种类)
    """

    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter
        counter = Counter(tasks)

        times = 0
        nums = [[i, 0] for i in counter.values()]
        for _ in tasks:
            # 找到剩余冷却时间最小的那个
            target = min(nums, key=lambda x: x[1] if x[0] > 0 else float('inf'))
            if target[1] > times:
                times = target[1]
            else:
                # 找到已经冷却且次数最大的那个
                target = max(nums, key=lambda x: x[0] if x[1] <= times else -1)
            target[0] -= 1
            times += 1
            target[1] = times + n
        return times


class Solution1:
    """
        这题真是无法理解....
    """

    def leastInterval(self, tasks: List[str], n: int) -> int:
        pass


s = Solution()
s.leastInterval(["A", "A", "A", "B", "B", "B", "B"], 2)
