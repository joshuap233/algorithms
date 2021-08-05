# https://leetcode-cn.com/problems/group-anagrams/
# 49. 字母异位词分组

from typing import List, Dict


class Solution:
    """
        字符串也可以用 sorted 方法排序,不过结果时是 list,
        然后用 dict 存取有序 string 即可(sorted 返回的 list 拼接)
    """

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        d: Dict[str, list] = {}
        for i in strs:
            s = ''.join(sorted(i))
            if s in d:
                d[s].append(i)
            else:
                d[s] = [i]
                res.append(d[s])
        return res


class Solution1:
    """
        collections 有一个 defaultdict  对象
        初始化时传入一个对象,
        当每个键第一次遇见时，它还没有在字典里面，所以自动创建该对象
    """

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        dct = defaultdict(list)
        for i in strs:
            s = "".join(sorted(i))
            dct[s].append(i)
        return list(dct.values())
