#  加一


class Solution:
    def plusOne(self, digits):
        number = ''
        for item in digits:
            number += str(item)
        number = list(str(int(number) + 1))
        return [int(item) for item in number]
