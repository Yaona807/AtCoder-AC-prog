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

def f(s,connect,n):
    from collections import deque

    visited = [False] * (n+1)
    q = deque()
    q.append(s)
    visited[s] = True
    cnt = [0]*(n+1)
    while q:
        now = q.popleft()

        for to in connect[now]:
            if visited[to]:
                continue
            visited[to] = True
            q.append(to)
            cnt[to] = cnt[now] + 1
    return cnt
# main関数
def main():
    n = readline_int()
    connect = [[]for _ in range(n+1)]
    for i in range(n-1):
        a,b = readline_int(True)
        connect[a].append(b)
        connect[b].append(a)
    
    cnt = f(1,connect,n)
    max_n1 = -1
    max_id1 = -1
    for i in range(1,n+1):
        if max_n1 < cnt[i]:
            max_n1 = cnt[i]
            max_id1 = i

    cnt = f(max_id1,connect,n)
    max_n2 = -1
    for i in range(1,n+1):
        max_n2 = max(max_n2,cnt[i])

    print(max_n2 + 1)            


        

if __name__ == '__main__':
    main()
