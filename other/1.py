def next_perm(nums: list) -> bool:
    n = len(nums)
    i = n - 2
    while i >= 0:
        if nums[i] < nums[i + 1]:
            break
        i -= 1

    if i < 0:
        return False

    j = 0
    for j in reversed(range(i + 1, n)):
        if nums[j] > nums[i]:
            break
    nums[j], nums[i] = nums[i], nums[j]
    k = -1
    for i in range(i + 1, (i + n) // 2 + 1):
        nums[i], nums[k] = nums[k], nums[i]
        k -= 1
    return True


def main():
    n = int(input())
    nums = map(lambda x: int(x), input().split())

    nums = sorted(nums)
    tmp = nums[:]

    cnt = 1
    while next_perm(nums):
        cnt += 1
    print(cnt)

    nums = tmp
    while True:
        for i in nums:
            print(i, end=' ')
        print('\n')
        if not next_perm(nums):
            break


main()
