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
    N,M,K = readline_int(True)
    A_list = readline_list_int()
    B_list = readline_list_int()
    index = 0
    check_list1 = [0 for _ in range(M+1)]
    for i in B_list:
        if check_list1[index] + i <= K:
            check_list1[index+1] = check_list1[index]+i
            index += 1
        else:
            break
    ans = index
    a_len = 0
    total = 0
    for i in A_list:
        if index > 0 and i + total + check_list1[index]> K:
            index -= 1
        total += i
        a_len += 1
        if total+check_list1[index] <= K:
            ans = max(index+a_len,ans)
    print(ans)        



if __name__ == '__main__':
    main()

