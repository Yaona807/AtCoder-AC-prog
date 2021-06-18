'''
文字列取得用関数
split=Trueを引数に渡すことにより、
mapで分割したものを戻り値とする
'''


from math import pi


def readline_str(split=False):
    import sys
    readline = sys.stdin.readline
    if split:
        return map(str, readline().rstrip().split())
    else:
        return readline().rstrip()


'''
整数取得用関数
split=Trueを引数に渡すことにより、
mapで分割したものを戻り値とする
'''
def readline_int(split=False):
    import sys
    readline = sys.stdin.readline
    if split:
        return map(int, readline().rstrip().split())
    else:
        return int(readline().rstrip())


'''
整数取得用関数(多次元配列)
Nに数値を渡すことにより、
N次元配列の値を取得可能
'''
def readline_list_int(N=1):
    if N == 1:
        return list(list(readline_int(True)))
    else:
        return list(list(readline_int(True))for _ in range(N))


'''
文字列取得用関数(多次元配列)
Nに数値を渡すことにより、
N次元配列の値を取得可能
また、split=Trueにより、
文字列を分割した状態で格納可能
'''
def readline_list_str(N=1, split=False):
    if split:
        return list(list(readline_str(True)) for _ in range(N))

    else:
        return list(list(readline_str()) for _ in range(N))

def f(num):
    from math import factorial
    cnt = [0]*10
    for i in range(len(num)):
        cnt[num[i]] += 1 
    ans = 1
    lengtn = len(num)
    n = lengtn - 1
    index = 0
    while n > 0:
        c = factorial(n)
        for i in range(len(num)):
            if (i+1) == num[index]:
                cnt[num[index]] -= 1
                break
            elif cnt[i+1] != 0:
                ans += c
        n -= 1
        index += 1
    return ans
	


# main関数
def main():
    n = readline_int()

    p = list(list(readline_int(True)))
    ans1 = f(p)
    q = list(list(readline_int(True)))
    ans2 = f(q)

    print(abs(ans1-ans2))


if __name__ == '__main__':
    main()
