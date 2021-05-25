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
    N = readline_list_str()
    total = 0
    num_list = [0,0,0]
    for i in N:
        num_list[int(i)%3] += 1
        total += int(i)
    mod = total % 3
    if mod == 0:
        print(0)
    elif num_list[mod] != 0 and len(N) != 1:
        print(1) 
    elif (num_list[1] >= 2 or num_list[2] >= 2) and len(N) >=3:
        print(2)
    else:
        print(-1)



    

    
if __name__ == '__main__':
    main()
