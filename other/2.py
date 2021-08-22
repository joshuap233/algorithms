from collections import defaultdict


def main(s: str, options: list):
    Dict = defaultdict(list)

    for j, v in enumerate(s):
        Dict[v].append(j + 1)

    for j, v in options:
        if int(j) == 1:
            s += v
            Dict[v].append(len(s))
        else:
            v = int(v)
            t = Dict[s[v - 1]]
            if len(t) <= 1:
                print(-1)
            else:
                k = t.index(v)
                mini = float('inf')
                if k > 0:
                    mini = min(mini, abs(t[k - 1] - v))
                if k < len(t) - 1:
                    mini = min(mini, abs(t[k + 1] - v))
                print(mini)


s = input()
n = int(input())
opt = []
for i in range(n):
    opt.append(input().split())
main(s, opt)
