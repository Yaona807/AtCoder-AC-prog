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
    t,N = readline_int(True)
    num_list = [False]*(101+t)
    num_list[0] = True
    cnt = 0
    ans = 0
    for i in range(1,len(num_list)):
        prime = int(((100 + t) * i / 100)//1) 
        if prime <= 100+t:
            num_list[prime] = True
    cnt = num_list.count(False)
    index = (N-1) % cnt
    for i in range(1,len(num_list)):
        if num_list[i]:
            continue
        if index == 0:
            ans = i + (100 + t) * ((N-1) // cnt)
            break
        index -= 1
    
    print(ans)

if __name__ == '__main__':
    main()

