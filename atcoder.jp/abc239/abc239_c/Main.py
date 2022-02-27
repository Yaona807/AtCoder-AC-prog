x1,y1,x2,y2 = map(int,input().split())
cross_point = [
  [-1,2],
  [-2,1],
  [-2,-1],
  [-1,-2],
  [1,-2],
  [2,-1],
  [2,1],
  [1,2]
]

for i in range(len(cross_point)):
  cp1 = [cross_point[i][0]+x1,cross_point[i][1]+y1]
  
  for j in range(len(cross_point)):
    cp2 = [cross_point[j][0]+x2,cross_point[j][1]+y2]
    if cp1 == cp2:
      print('Yes')
      exit()
      
print('No')