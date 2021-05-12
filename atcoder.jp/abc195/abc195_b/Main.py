def main():
    import sys

    # 入力
    readline = sys.stdin.readline
    A,B,W = map(int,readline().rstrip().split())
    W = W * 1000
    ax = int(W // A)
    bx = int(-(-W // B))
    x = W - (A * ax)
    if ax >= bx:
        print(bx,ax)
    else:
        print('UNSATISFIABLE')

main()
