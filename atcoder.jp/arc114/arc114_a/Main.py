def main():
    import sys

    readline = sys.stdin.readline
    # 入力
    N = int(readline().rstrip())
    ans = 100000000000000000000
    X = list(list(map(int,readline().rstrip().split())))
    prime_list = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
    for i in range(2**len(prime_list)):
        count = 1
        for j in range(len(prime_list)):
            if ((i >> j) & 1):
                count *= prime_list[j]
        for j in X:
            flag = 0
            for k in prime_list:
                if count % k == 0 and j % k == 0:
                    flag = 1
                    break
            if flag == 0:
                flag = 2
                break
        if flag != 2:
            ans = min(ans,count)
            
            
        
    print(ans)
main()
