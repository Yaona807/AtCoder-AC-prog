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

#nの約数を全て求める
def divisor(n): 
    i = 1
    table = []
    while i * i <= n:
        if n%i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = list(set(table))
    return table

# main関数
def main():
    N = readline_int()
    A_list = readline_list_int()
    cnt_list = [0 for _ in range(max(A_list)+1)]
    for i in A_list:
        table = divisor(i)
        for j in table:
            cnt_list[j] += 1
    ans = 0
    max_num = 0
    for i in range(len(cnt_list)):
        if i != 1 and max_num <= cnt_list[i]:
            max_num = cnt_list[i]
            ans = i
    print(ans)

    

    
if __name__ == '__main__':
    main()
