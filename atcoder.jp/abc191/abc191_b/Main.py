def main():
    import sys

    # 入力
    readline = sys.stdin.readline
    N,X = map(int,readline().rstrip().split())
    A_list = list(readline().rstrip().split())
    #A_list = list(list(map(str,readline().rstrip().replace(str(X),''))))
    # A = readline().rstrip().replace(str(X),'')
    j = 0
    for i in A_list:
        j += 1
        if i != str(X): 
            print(i,end='')
            if j != len(A_list):
                print(end = ' ')
main()
