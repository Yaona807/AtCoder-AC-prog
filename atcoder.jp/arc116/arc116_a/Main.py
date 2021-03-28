def main():
    import sys
    readline = sys.stdin.readline
    # 入力
    T = int(readline().rstrip())
    case = list(int(readline().rstrip())for _ in range(T))
    for i in case:
        if i % 2 != 0:
            print('Odd')
        elif (i//2) % 2 == 0:
            print('Even')
        else:
            print('Same')
    
main()