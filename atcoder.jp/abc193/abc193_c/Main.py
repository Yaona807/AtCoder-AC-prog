def main():
    import sys

    readline = sys.stdin.readline

    n = int(readline().rstrip())
    ans = set()
    for i in range(2,n+1):
        j = 1
        a = i * i
        if a > n:
            break
        while a <= n:
            ans.add(a)
            a *= i
    print(n - len(ans))
main()