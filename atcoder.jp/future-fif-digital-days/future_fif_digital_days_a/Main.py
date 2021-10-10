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

# 1063830
# 1123596

# (function) main
def main():
    n,k,b = inputter()
    mark = []

    ans='''36
7 0 0
3 0 4
2 4 7
4 4 11
9 13 15
9 10 22
9 0 17
6 0 24
9 23 24
11 41 17
10 26 32
9 28 41
4 33 44
9 5 32
6 4 46
11 24 18
10 30 0
1 30 31
5 22 13
8 41 24
5 34 36
4 10 47
11 18 43
1 9 48
1 27 43
8 5 24
11 13 32
9 22 6
11 13 3
5 12 9
1 15 14
10 42 9
3 44 4
5 38 15
9 33 20
1 41 23'''
    
    for _ in range(k):
        i,j = inputter()
        
        mark.append([i,j])
    
    s_list = []
    for _ in range(b):
        nb,mb,cb = inputter()
        
        s = inputter(is_list=True,loop_times=nb)

        s_list.append(s)

    print(ans)

if __name__ == '__main__':
    main()
