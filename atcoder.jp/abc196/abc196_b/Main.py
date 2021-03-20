def main():
    import sys
 
    readline = sys.stdin.readline
    # 入力
    X = list(readline().rstrip())
    x = 0
    str_x = ''
    if '.' in X:
        x = X.index('.')
        for i in range(x):
            str_x = str_x + X[i]
    else:
        for i in range(len(X)):
            str_x = str_x + X[i]
    print(int(str_x))
main()