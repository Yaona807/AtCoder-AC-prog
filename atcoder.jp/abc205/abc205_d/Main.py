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

# main関数
def main():
    n,q = readline_int(True)
    a = list(list(readline_int(True)))
    c = [0]*(n+1)
    for i in range(n):
        c[i + 1] = a[i] - (i + 1)

    for _ in range(q):
        k = readline_int()
        left = 0
        right = len(c)
        while abs(left-right) !=1:
            mid = (left+right)//2
            if c[mid] >= k:
                right = mid
            else:
                left = mid
        if right == 1:
            ans = k
        else:
            ans = a[right-2]+(k-c[right-1])
        print(ans)



if __name__ == '__main__':
    main()
