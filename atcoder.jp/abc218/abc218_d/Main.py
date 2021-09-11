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

# (function) main
def main():
    from collections import defaultdict
    n = inputter()
    d = defaultdict(list)
    for _ in range(n):
        x,y = inputter()
        d[x].append(y)
    X = list(d.keys())
    ans = 0
    for i in range(len(X)):
        if len(d[X[i]]) == 1:
            continue
        for j in range(i+1,len(X)):
            if len(d[X[j]]) == 1:
                continue
            cnt = 0
            max_len = max(len(d[X[j]]),len(d[X[i]]))
            if max_len == len(d[X[j]]):
                flag = 1
            else:
                flag = 2
            for k in range(max_len):
                if flag == 2 and d[X[j]].count(d[X[i]][k]) == 1:
                    cnt += 1
                if flag == 1 and d[X[i]].count(d[X[j]][k]) == 1:
                    cnt += 1
            ans += (cnt*(cnt-1))//2
    print(ans)



if __name__ == '__main__':
    main()
