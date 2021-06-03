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
    Q = readline_int()
    Q_list = list(list(readline_int(True))for _ in range(Q))
    cnt_list = [0]*(pow(10,5)+1)
    total = 0
    ans_list = []
    for i in A_list:
        cnt_list[i] += 1
        total += i

    for i in Q_list:
        B,C = i[0],i[1]
        total += (C-B) * cnt_list[B]
        cnt_list[C] += cnt_list[B]
        cnt_list[B] = 0
        ans_list.append(total)
    
    for i in ans_list:
        print(i)



if __name__ == '__main__':
    main()

