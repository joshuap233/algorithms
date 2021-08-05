解决问题的方法:

1. 举例,比如列举输入数据,如果是你(人), 该怎么做,才能得到想要的结果

2. 思考可能需要的辅助数据结构

3. 列举可能的解决方案(数据结构),然后找到这些方案的问题

4. 先写暴力解法，再优化,(动态规划,先暴力,再剪枝

5. 题目没写出来前,别瞎优化

6. 遇到判定条件可以举例判断

TODO: 整理用到的数据结构,以及 Python 内置的数据结构

注意求中位数的方法:

```python
def findMedianSortedArrays(nums1, nums2) -> float:
    new = nums2 + nums1

    # 归并
    new.sort()
    mid = len(new) // 2
    if len(new) % 2 == 0:
        return (new[mid] + new[mid - 1]) / 2
    return new[mid]

# array[mid] 
# 或
# (array[mid-1] + array[mid])/2
```

需要注意的题(恶心题):

剑指 Offer 20. 表示数值的字符串:
https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof/

剑指 Offer 62. 圆圈中最后剩下的数字
https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/

剑指 Offer 19. 正则表达式匹配
https://leetcode-cn.com/problems/zheng-ze-biao-da-shi-pi-pei-lcof/

剑指 Offer 43. 1～n 整数中 1 出现的次数
https://leetcode-cn.com/problems/1nzheng-shu-zhong-1chu-xian-de-ci-shu-lcof/

剑指 Offer 65. 不用加减乘除做加法
https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/

剑指 Offer 56 - II. 数组中数字出现的次数 II
https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-ii-lcof/

剑指 Offer 51. 数组中的逆序对
https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/
