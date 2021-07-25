# -*- coding: utf-8 -*-

'''
Function to get a string.
--
is_str:bool -> {
    True: input data is 'str'.
    False: input data is not 'str'.
    *This function can determine the type automatically.
}
split:bool ->{
    True: Split the input data.
    False: Does not split the input data.
    *This function can automatically determine the split.
}
is_list:bool ->{
    True: Get input data in a list.
    False: Does not get input data in a list
}
loop_times:int ->{
    Used when input data is to be retrieved multiple times.
}

'''
from sys import flags


def inputter(is_str=False, split=False, is_list=False, loop_times=0):
    import sys
    readline = sys.stdin.readline

    return_data_list = []
    loop_cnt = loop_times

    # Adjusting for processing
    if loop_times == 0:
        loop_cnt = 1

    for _ in range(loop_cnt):
        # Get input data
        data = readline().rstrip()
        data_split = data.split()

        # Determine if input data can be split
        if not(split) and len(data_split) > 1:
            split = True

        # Determine the type of input data
        if not(is_str):
            try:
                int(data_split[0])
            except:
                is_str = True

        # Process according to input data
        if is_str:
            if split:
                if is_list:
                    return_data = list(list(map(str, data_split)))
                else:
                    return_data = map(str, data_split)
            else:
                if is_list:
                    return_data = list(data)
                else:
                    return_data = data
        else:
            if split:
                if is_list:
                    return_data = list(list(map(int, data_split)))
                else:
                    return_data = map(int, data_split)
            else:
                if is_list:
                    return_data = list(list(int(data)))
                else:
                    return_data = int(data)

        # Only when input data is to be acquired multiple times
        if loop_times != 0:
            return_data_list.append(return_data)

    # Return the result
    if loop_times == 0:
        return return_data
    else:
        return return_data_list

# (function) main
def main():
    from collections import deque

    n,m = inputter()
    mod = pow(10,9) + 7
    inf = 10101010010100101
    G = [[]for _ in range(n)]
    cnt = [[inf,0] for _ in range(n)]
    q = deque()

    for _ in range(m):
        a,b = inputter()
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    
    q.append(0)
    cnt[0][0] = 0
    cnt[0][1] = 1

    # bfs
    while q:
        now = q.popleft()

        for to in G[now]:
            # 未到達なら'深さ+1','カウント同値'で更新
            # 根を展開する
            if inf == cnt[to][0]:
                cnt[to][0] = (cnt[now][0] + 1) % mod
                cnt[to][1] = cnt[now][1]
                q.append(to)
            # 到達済みは更新可能(深さが同じ)ならば、カウントの値のみ更新
            # 一度展開しているので、再度の展開はなし
            elif cnt[to][0] == cnt[now][0] + 1:
                cnt[to][1] += (cnt[now][1]) % mod
    
    print(cnt[n-1][1]%mod)

if __name__ == '__main__':
    main()
