def main():
    import sys

    readline = sys.stdin.readline
    # 入力
    N,L = map(int,readline().rstrip().split())
    X_A=list(list(map(int,readline().rstrip().split())) for _ in range(N))
    ans = 0
    x = 0
    flag = 0
    for i in X_A:
        X = i[0]
        A = i[1]
        ans -= A
        if flag != 0:
            ans += X - x
        x = X
        flag = 1
    
    T = abs(ans)
    t = T
    x = 0
    flag = 0

    while True:
        for i in X_A:
            if t < T:
                t += i[0] - x
                if t > T:
                    t = T
            t -= i[1]
            x = i[0]
            if t < 0:
                flag = 1
                break
        if flag == 1:
            T = T + 1
            t = T
            x = 0
            flag = 0
        else:
            ans = T
            break

    t = T
    x = 0
    flag = 0
    while True:
        for i in X_A:
            if t < T:
                t += i[0] - x
                if t > T:
                    t = T
            t -= i[1]
            x = i[0]
            if t < 0:
                flag = 1
                break
        if flag == 0:
            ans = T
            T = T - 1
            t = T
            x = 0
            flag = 0
        else:
            break

    print(ans)
main()