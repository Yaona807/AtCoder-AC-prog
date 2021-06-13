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
    n,l = readline_int(True)
    k = readline_int()
    a = list(list(readline_int(True)))

    left = -1
    right = l + 1
    while abs(left-right)!=1:
        mid = (left+right)//2
        cnt = 0
        num = 0
        for i in range(len(a)):
            if mid <= a[i]-num and l - a[i] >= mid:
                cnt += 1
                num = a[i]
        if cnt < k:
            right = mid
            mid =(left+right)//2
        else:
            left = mid
            mid =(left+right)//2

    print(left)

        



if __name__ == '__main__':
    main()
