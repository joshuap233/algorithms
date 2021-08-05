# https://leetcode-cn.com/problems/implement-trie-prefix-tree/
# 208. 实现 Trie (前缀树)

from typing import Dict


class Trie:
    """
        用嵌套字典实现.....,
        也可以用数组实现....毕竟只有 26 个字母...
    """

    def __init__(self):
        self.mp: Dict[str:Dict] = {}
        self.end = '$'

    def insert(self, word: str) -> None:
        d = self.mp
        for i in word:
            d.setdefault(i, {})
            d = d[i]
        d[self.end] = {}

    def search(self, word: str) -> bool:
        d = self.mp
        for i in word:
            if i not in d:
                return False
            d = d[i]
        return True if self.end in d else False

    def startsWith(self, prefix: str) -> bool:
        d = self.mp
        for i in prefix:
            if i not in d:
                return False
            d = d[i]
        return True

s = Trie()
s.insert("apple")
