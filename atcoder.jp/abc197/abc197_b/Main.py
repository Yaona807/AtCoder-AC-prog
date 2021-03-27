def main():
    import sys

    readline = sys.stdin.readline
    # 入力
    H,W,X,Y = map(int,readline().rstrip().split())
    S = list(list(readline().rstrip()) for _ in range(H))

    x = X - 1
    y = Y - 1
    count = 1
    i = x
    j = y
    while True:
        i += 1
        if i >= H or S[i][j] == '#':
            break
        count += 1
    i = x
    j = y
    while True:
        i -= 1
        if i < 0 or S[i][j] == '#':
            break
        count += 1
    i = x
    j = y
    while True:
        j += 1
        if j >= W or S[i][j] == '#':
            break
        count += 1
    i = x
    j = y
    while True:
        j -= 1
        if j < 0 or S[i][j] == '#':
            break
        count += 1
    print(count)
main()