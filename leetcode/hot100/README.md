需要更优解:
T4

想到某种算法前,先举例子验证,最好是特殊的例子

和数组,字符串边界,长度有关的题可以设置一个 left 与 right

一个有意思的数据结构: 单调栈:
单调栈适合的题目是求解下一个大于 xxx或者下一个小于 xxx这种题目。
所有当你有这种需求的时候，就应该想到单调栈。


回溯: 利用递归返回来继续使用之前的状态, 和深搜很像

递归注意注意函数调用顺序,需要回溯的代码在深搜的代码之后....

各种动态规划题需要重新做一遍

,用切片遍历似乎更浪费空间

leetcode 执行用时根本不靠谱,,,,,,,

heapq 如果 push 一个元素,第一个元素为排序索引

set 中不能添加 list: unhashable type

lru_cache 装饰的函数参数不能为 dict,list 理由也是 unhashable type

分析回溯题的时候画出一棵树,用于分析与剪枝

类型相同的题:

https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof/
剑指 Offer 59 - II. 队列的最大值

https://leetcode-cn.com/problems/daily-temperatures/
739. 每日温度

https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof/
剑指 Offer 30. 包含min函数的栈

维护递增或递减队列,栈
