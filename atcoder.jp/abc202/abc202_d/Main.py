def main():
    import sys
    import math

    #入力
    readline = sys.stdin.readline
    A,B,K = map(int,readline().rstrip().split())
    ans = ''
    while True:
        c = 0
        if A >= 1:
            n = A + B - 1
            r = A - 1
            c = math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
        if c >= K:
            ans += 'a'
            A -= 1
        else:
            B -= 1
            ans += 'b'
            K -= c
        if A + B == 0:
            break
    print(ans)


main()
