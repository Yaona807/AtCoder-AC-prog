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

ans = []
def dfs(now,G,visited):
    ans.append(now)
    visited[now] = True
    for to in G[now]:
        if visited[to]:
            continue
        dfs(to,G,visited)
        ans.append(now)
    return

# (function) main
def main():
    import sys
    sys.setrecursionlimit(pow(10,8))
    n = inputter()
    G = [[]for i in range(n+1)]
    visited = [False for i in range(n+1)]
    for i in range(n-1):
        a,b = inputter()
        G[a].append(b)
        G[b].append(a)
    for i in range(1,n+1):
        G[i].sort()
    dfs(1,G,visited)
    print(*ans)

if __name__ == '__main__':
    main()