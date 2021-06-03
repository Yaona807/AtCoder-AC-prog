'''
文字列取得用関数
split=Trueを引数に渡すことにより、
mapで分割したものを戻り値とする
'''


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
    N = readline_int()
    A_list = readline_list_int()
    ans_min = 10100101010101010101
    for i in range(pow(2,N-1)):
        ans_or = A_list[0]
        ans_xor = 0
        for j in range(1,N):
            if (i >> (j-1))&1:
                ans_xor ^= ans_or
                ans_or = 0
            ans_or |= A_list[j]
        ans_xor ^= ans_or
        ans_min = min(ans_min,ans_xor)
    
    print(ans_min)



if __name__ == '__main__':
    main()

