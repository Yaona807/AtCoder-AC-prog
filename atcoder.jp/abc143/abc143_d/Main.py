# -*- coding: utf-8 -*-

'''
文字列取得用関数(str,int併用)
'''
def inputter(is_str=False,split=False):
    import sys
    readline = sys.stdin.readline
    
    if is_str:
        if split:
            return map(str, readline().rstrip().split())
        else:
            return readline().rstrip()
    else:
        if split:
            return map(int, readline().rstrip().split())
        else:
            return int(readline().rstrip())

'''
二重リストを返す関数
'''
def double_list(input_data):
    return list(list(input_data))

# main関数
def main():
    n = inputter()
    l = list(list(inputter(0,1)))
    l.sort(reverse=True)
    cnt = 0
    for a in range(n - 2):
        for b in range(a+1,n - 1):
            # -c < a-b < c < a + b
            if not(-l[b+1] < l[a] - l[b] < l[b + 1] < l[a] + l[b]):
                break
            ok = b
            ng = n
            while abs(ok - ng) > 1:
                mid = (ok + ng) // 2
                if -l[mid] < l[a] - l[b] < l[mid] < l[a] + l[b]:
                    ok = mid
                else:
                    ng = mid
            cnt += ok - b
    print(cnt)
    
if __name__ == '__main__':
    main()