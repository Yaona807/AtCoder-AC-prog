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
    n,m,x = readline_int(True)
    data = list(list(readline_int(True)) for _ in range(n))
    ans = 10101010101010
    for i in range(pow(2,n)):
        judge = [0]*m
        total = 0
        flag = 0
        for j in range(n):
            if (i >> j)&1:
                total += data[j][0]
                for k in range(m):
                    judge[k] += data[j][k+1]
        for k in range(m):
            if judge[k] < x:
                flag = 1
                break
        if flag == 0:
            ans = min(ans,total)
    if ans == 10101010101010:
        print(-1)
    else:
        print(ans)





    

if __name__ == '__main__':
    main()

