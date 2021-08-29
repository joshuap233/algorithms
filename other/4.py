coin = [64, 16, 4, 1]


def main(n: int):
    n = 1024 - n
    cnt = 0
    for i in coin:
        cnt += n // i
        n %= i
    print(cnt)


inp = int(input())
main(inp)
