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
    S_list = [[readline_str()]for _ in range(N)]
    s_list = []
    for i in range(N):
        s_list.append([S_list[i][0],int(S_list[i][0]),len(S_list[i][0])])
    s_list = sorted(s_list,reverse=True, key=lambda x:x[2])
    s_list = sorted(s_list,key=lambda x:x[1])
    
    for i in s_list:
        print(i[0])

if __name__ == '__main__':
    main()

