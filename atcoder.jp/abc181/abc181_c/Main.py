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
    import sys
    readline = sys.stdin.readline
    if N == 1:
        return list(list(map(int, readline().rstrip().split())))
    else:
        return list(list(map(int, readline().rstrip().split()))for _ in range(N))


'''
文字列取得用関数(多次元配列)
Nに数値を渡すことにより、
N次元配列の値を取得可能
また、split=Trueにより、
文字列を分割した状態で格納可能
'''
def readline_list_str(N=1, split=False):
    import sys
    readline = sys.stdin.readline
    if N == 1:
        if split:
            return list(readline().rstrip().split())
        else:
            return list(readline().rstrip())
    else:
        if split:
            return list(list(readline().rstrip().split())for _ in range(N))

        else:
            return list(list(readline().rstrip())for _ in range(N))


# main関数
def main():
    N = readline_int()
    flag = 0
    x_list = [0]*N
    y_list = [0]*N
    for i in range(N):
        x,y = readline_int(True)
        x_list[i] = x
        y_list[i] = y
    for i in range(N-2):
        for j in range(i+1,N-1):
            x = x_list[j] - x_list[i]
            if x == 0:
                m1 = float('inf') 
            else:
                y = y_list[j]-y_list[i]
                m1 = y / x
            for k in range(j+1,N):
                x = x_list[k] - x_list[j]
                if x == 0:
                    m2 = -float('inf')
                else:
                    y = y_list[k]-y_list[j]
                    m2 = y / x
                if m1 == m2 or (x_list[i] == x_list[j] == x_list[k]) or (y_list[i] == y_list[j] == y_list[k]):
                    print('Yes')
                    exit()
    print('No')


if __name__ == '__main__':
    main()
