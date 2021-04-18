def main():
    import sys
    readline = sys.stdin.readline
    # 入力
    A,B = map(int,readline().rstrip().split())
    a = 0
    b = 0
    for i in range(1,A):
        a += i
    for i in range(1,B):
        b += i
    x = A
    y = B
    while True:
        if (x+a) - (y+b) > 0:
            y += 1
        elif (x+a) - (y+b) < 0:
            x += 1
        else:
            break
    for i in range(1,A):
        print(i,end=' ')
    for i in range(1,B):
        print(-i,end=' ')
    print(x,-y)
main()