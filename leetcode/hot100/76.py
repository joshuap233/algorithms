# https://leetcode-cn.com/problems/minimum-window-substring/
# 76. 最小覆盖子串
from collections import Counter


class Solution:
    """
        我只想到了 O(n*n) 的暴力算法....

        我觉得我做过这题....或者某题我用过类似的解法...

        思路我有..一写就错...
        思路:
            设置 left ,right 指针,
            right 指针左移,直到包含了所有在 t 中的元素,
            left 指针左移,去除不需要的元素,然后计算最大值
            (存储当前left与 right),然后 left 指针左移 1 次,重复上面的操作
        使用一个哈希表存储: cnt 为 0 则恰好符号要求,
        cnt > 0 则还需要 cnt 个该字符, cnt<0 则多了 cnt个该字符

        写了半天,边界一写就错.....真他妈恶心
    """

    def minWindow(self, s: str, t: str) -> str:
        window = Counter(t)
        need = len(t)
        res = [0, float('inf')]
        left = 0

        for right, v in enumerate(s):
            if v in window:
                if window[v] > 0:
                    need -= 1
                window[v] -= 1

            if need == 0:
                while True:
                    u = s[left]
                    if u in window and window[u] == 0:
                        break
                    if window[u] < 0:
                        window[u] += 1
                    left += 1

                if right - left < res[1] - res[0]:
                    res[:] = left, right

                window[s[left]] += 1
                need += 1
                left += 1
        return '' if res[1] > len(s) else s[res[0]:res[1] + 1]


s = Solution()
s.minWindow("a", "aa")
