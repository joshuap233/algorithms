# https://leetcode-cn.com/problems/queue-reconstruction-by-height/
# 406. 根据身高重建队列

from typing import List


class Solution:
    """
        这题看着就是排序题,无非就是找到排序的键,然后稍微修改下
        ....
        居然交一次就对了

        简单说就是先排序,在插队....首先按照身高降序排序...
        身高相同的按照 k 升序排列
        然后遍历一遍, 元素插入到索引为 k 的位置....

        高的在前面..矮的插入到高的前面不会影响前面人的 k
    """

    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 按照身高降序排序...身高相同的按照 k1 升序排列
        people.sort(key=lambda x: (-x[0], x[1]))

        j = 0
        while j < len(people):
            _, index = people[j]
            if index < j:
                people.insert(index, people[j])
                people.pop(j + 1)
            j += 1
        return people


class Solution1:
    """上面的优化"""

    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        res = []
        for p in people:
            res.insert(p[1], p)
        return res


s = Solution()
s.reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]])
