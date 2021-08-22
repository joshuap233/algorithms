def main(s):
    multi = 1
    stack = []

    for i in s:
        if i == '(':
            if stack:
                stack[-1][1] = 1
            stack.append([multi, 2])
            multi = 1
        else:
            last_multi, v = stack.pop(-1)
            multi = last_multi * v
    if not stack:
        print(multi)


ss = input()
main(ss)
