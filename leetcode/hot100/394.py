# https://leetcode-cn.com/problems/decode-string/
# 394. 字符串解码

"""
你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，
例如不会出现像 3a 或 2[4] 的输入。
"""


class Solution:
    """
        使用辅助栈,这题难点在 嵌套,比如 2[a2[c]],需要从内向外拼接字符

        我的解法会将 倍数,[,] 与 字符都加入栈中
        我自己的解法,太恶心了....
    """

    def decodeString(self, s: str) -> str:
        stack = []

        i = 0
        while i < len(s):
            if s[i].isdigit():
                left = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                stack.append(int(s[left:i]))
            elif s[i] == '[':
                stack.append(s[i])
                i += 1
            elif s[i] == ']':
                r = ''
                while (e := stack.pop()) != '[':
                    r = e + r
                stack.append(stack.pop() * r)
                i += 1
            else:
                left = i
                while i < len(s) and 'a' <= s[i] <= 'z':
                    i += 1
                stack.append(s[left:i])
        return ''.join(stack)


class Solution1:
    """
        上面的代码优化
        在栈中存储两个信息,
            1. 左括号前的字符串,
            2. 左括号前的数字
            (a,b)
        遇到左括号将上面两个数入栈,清空,
        遇到右括号弹出,栈中左括号前的字符串实际上是上一次的字符串
    """

    def decodeString(self, s: str) -> str:
        stack = []

        res, multi = '', 0
        for i in s:
            if i.isdigit():
                multi = multi * 10 + int(i)
            elif i == '[':
                stack.append((res, multi))
                res, multi = '', 0
            elif i == ']':
                last_res, cur_multi = stack.pop()
                res = last_res + cur_multi * res
            else:
                res += i
        return res
