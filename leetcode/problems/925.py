# 925. 长按键入
# 　https://leetcode-cn.com/problems/long-pressed-name/
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if name[0] != typed[0]:
            return False
        name_index = 1
        for index in range(1, len(typed)):
            if name_index >= len(name) or typed[index] != name[name_index]:
                pre_typed = typed[index - 1]
                if pre_typed != typed[index]:
                    return False
            else:
                name_index += 1
        if name_index >= len(name):
            return True
        return False


s = Solution()
print(s.isLongPressedName("pyplrz", "ppyypllr"))
