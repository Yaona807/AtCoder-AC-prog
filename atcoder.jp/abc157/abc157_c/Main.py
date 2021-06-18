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
    n,m = readline_int(True)
    ans = -1
    num = [-1] * n
    flag = 0
    for _ in range(m):
        s,c = readline_int(True)
        if num[s-1] != -1 and num[s-1] != c:
            flag = 1
        num[s-1] = c
    if flag == 1:
        print(ans)
        exit()
    num.reverse()
    for i in range(1000):
        num_s = list(str(i))
        num_s.reverse()
        flag = 0
        for j in range(len(num_s)):
            if int(num_s[j]) != num[j] and num[j] != -1:
                flag = 1
                break
        if flag == 0 and n == len(str(i)):
            ans = i
            break

    print(ans)


if __name__ == '__main__':
    main()
