# https://ac.nowcoder.com/acm/contest/6488/A


#
# 解密密文
# @param str string字符串 密文
# @param d int整型 偏移量
# @return string字符串
#
class Solution:
    books = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

    def decode(self, string: str, d):
        book = self.str_dic()
        res = ''
        for index, item in enumerate(string):
            res = res + self.books[(book[item] - d) % len(self.books)]
        return res

    def str_dic(self):
        d = {}
        for index, item in enumerate(self.books):
            d[item] = index
        return d


s = Solution()
print(s.decode("pqyeqfgt", 200))
