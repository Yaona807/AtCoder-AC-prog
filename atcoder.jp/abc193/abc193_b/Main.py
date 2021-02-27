def main():
    import sys

    readline = sys.stdin.readline

    n = int(readline().rstrip())
    a_p_x = sorted((list(list(map(int,readline().rstrip().split()))for _ in range(n))))
    t = 0
    i = 0
    price = 10**10
    for i in a_p_x:
        if i[2] - i[0] > 0:
            price = min(price,i[1])
    if price == 10**10:
        print(-1)
    else:
        print(price)

main()
