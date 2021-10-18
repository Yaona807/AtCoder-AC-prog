n = int(input())
h_list = list(map(int,input().split()))

cnt = 0
while h_list.count(0) != n:
  flag = False
  
  for i in range(n):
    if h_list[i] != 0:
      flag = True
      h_list[i] -= 1
      continue
     
    if flag:
      cnt += 1
      flag = False
      
  if flag:
  	cnt += 1
    
print(cnt)
    
    