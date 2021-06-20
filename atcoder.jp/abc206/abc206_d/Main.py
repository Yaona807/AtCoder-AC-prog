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

def dfs(now,connect,visited,ans):
    for to in connect[now]:
        if visited[to]:
            continue
        visited[to] = True
        ans += 1
        ans,visited = dfs(to,connect,visited,ans)
    return ans,visited




# main関数
def main():
    import sys
    sys.setrecursionlimit(pow(10,9))

    n = readline_int()
    a = list(list(readline_int(True)))
    connect = [[] for _ in range((2*pow(10,5) + 1))]
    visited = [False for _ in range((2*pow(10,5) + 1))]
    for i in range(n//2):
        connect[a[i]].append(a[n-i-1])
        connect[a[n-i-1]].append(a[i])
    
    ans = 0
    for now in a:
        if visited[now]:
            continue
        visited[now] = True
        ans,visited = dfs(now,connect,visited,ans)
    print(ans)



if __name__ == '__main__':
    main()
