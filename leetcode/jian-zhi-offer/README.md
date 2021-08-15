

TODO: 整理用到的数据结构,以及 Python 内置的数据结构

注意求中位数的方法:

```python
def findMedianSortedArrays(new: list) -> float:
    new.sort()
    mid = len(new) // 2
    if len(new) % 2 == 0:
        return (new[mid] + new[mid - 1]) / 2
    return new[mid]
```

















