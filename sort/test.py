from random import randint


def random_lists(mini: int = 0, maxi: int = 1000, nums: int = 1000):
    return [randint(mini, maxi + 1) for _ in range(randint(0, nums + 1))]
