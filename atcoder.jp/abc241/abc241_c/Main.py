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

from re import L, search


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

def search(x,y,S,dx,dy,N):
    cnt = 0
    
    if N - (x + 5*dx) <= 0 or N - (y + 5*dy) <= 0:
        return False

    for i in range(6):
        if S[y][x] == '#':
            cnt += 1
        x += dx
        y += dy

        if x < 0 or y < 0:
            return False

    if cnt >= 4:
        return True
    else:
        return False

# (function) main
def main():
    import pprint
    N = inputter()

    S = [inputter(is_list=True)for _ in range(N)]

    dx = [0,1,0,-1,1,-1,-1,1]
    dy = [1,0,-1,0,1,1,-1,-1]

    for y in range(N):
        for x in range(N):
            for i in range(8):
                if search(x,y,S,dx[i],dy[i],N):
                    print('Yes')
                    return

    print('No')

if __name__ == '__main__':
    main()

