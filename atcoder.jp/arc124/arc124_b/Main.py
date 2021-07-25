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
    import collections
    n = inputter()
    a_list = inputter(split=True,is_list=True)
    b_list = inputter(split=True,is_list=True)
    zero_list = [0 for _ in range(n)]
    num = set()
    for i in range(n):
        num.add(a_list[0]^b_list[i])
    num_list = list(num)
    ans = []
    a_cnt = collections.Counter(a_list)
    for i in range(len(num_list)):
        a_dict = dict(zip(a_list,zero_list))
        flag = 0
        for j in range(n):
            x = b_list[j] ^ num_list[i]
            if x in a_dict:
                a_dict[x] += 1
            else:
                break
        for j in a_list:
            if a_dict[j] != a_cnt[j]:
                flag = 1
                break
        if flag == 0:
            ans.append(num_list[i])
    ans = list(set(ans))
    new_ans = sorted(ans)
    len_ans = len(new_ans)
    if len_ans == 0:
        print(0)
    else:
        print(len_ans)
        for i in new_ans:
            print(i)


if __name__ == '__main__':
    main()
