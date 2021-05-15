def main():
    import sys

    # 入力
    readline = sys.stdin.readline
    A_list = list(list(map(int,readline().rstrip().split())))
    A_list.sort()
    if abs(A_list[0]-A_list[1]) == abs(A_list[1]-A_list[2]):
        print('Yes')
    else:
        print('No') 

main()
