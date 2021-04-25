#移動先のチェック
def check_move(t_list,check_move_set,x,y,W,H):
    if x < 0 or x >= W:
        return False
    if y < 0 or y >= H:
        return False
    if t_list[y][x] in check_move_set:
        return False
    else:
        return True

def main():
    import sys
    readline = sys.stdin.readline
    # 入力
    s_i,s_j = map(int,readline().rstrip().split())
    move_list = [[1,0],[0,-1],[-1,0],[0,1]]#LDUR
    ans = ['D','L','U','R']
    ans_list = []
    H = W = 50
    t_list = list(list(map(int,readline().rstrip().split()))for _ in range(H))
    p_list = list(list(map(int,readline().rstrip().split()))for _ in range(H))
    check_move_set = set()
    check_move_set.add(t_list[s_i][s_j])
    flag = 0
    while True:
        for i in range(len(move_list)):
            if check_move(t_list,check_move_set,s_j + move_list[i][1],s_i+move_list[i][0],W,H):
                s_i += move_list[i][0]
                s_j += move_list[i][1]
                ans_list.append(ans[i])
                check_move_set.add(t_list[s_i][s_j])
                if s_i > 35:
                    ans[0],ans[1],ans[2],ans[3]=ans[2],ans[1],ans[3],ans[0]
                    move_list[0],move_list[1],move_list[2],move_list[3] = move_list[2],move_list[1],move_list[3],move_list[0]
                elif s_j < 5:
                    ans[0],ans[1],ans[2],ans[3]=ans[0],ans[2],ans[3],ans[1]
                    move_list[0],move_list[1],move_list[2],move_list[3] = move_list[0],move_list[2],move_list[3],move_list[1]
                break
            elif i == len(move_list) - 1:
                flag = 1
        if flag == 1:
            break
    for i in ans_list:
        print(i,end='')

    
 
main()