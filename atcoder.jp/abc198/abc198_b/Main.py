def main():
    import sys
    readline = sys.stdin.readline
    # 入力
    N = list(readline().rstrip())
    n = N[::-1]
    flag = 0
    j = 0
    for i in range(len(N)):
        if flag == 0 and n[i] == '0':
            continue
        elif flag == 0 and n[i] != '0':
            flag = 1
        if flag == 1 and n[i] != N[j]:
            flag = 2
            break
        else:
            j += 1
    if flag != 2:
        print('Yes')
    else:
        print('No')
main()