import sys

T = int(sys.stdin.readline().strip())


arr = [(1,1,1,0,1,1,1),(0,0,1,0,0,1,0),(1,0,1,1,1,0,1),(1,0,1,1,0,1,1),\
       (0,1,1,1,0,1,0),(1,1,0,1,0,1,1),(1,1,0,1,1,1,1),(1,1,1,0,0,1,0),(1,1,1,1,1,1,1),(1,1,1,1,0,1,1),(0,0,0,0,0,0,0)]
    

for t in range(T):
    A,B = map(int,sys.stdin.readline().split())
    cnt = 0
    arr_A = []
    arr_B = []
    str_A = "_"*(5-len(str(A)))+str(A)
    str_B = "_"*(5-len(str(B)))+str(B)
    for s in str_A:
        if s=='_':
            arr_A.append(arr[10])
        else:
            arr_A.append(arr[int(s)])
    for s in str_B:
        if s=='_':
            arr_B.append(arr[10])
        else:
            arr_B.append(arr[int(s)])
        
                
    for i in range(5):
        for j in range(7):
            if arr_A[i][j]!=arr_B[i][j]:
                cnt+=1
    sys.stdout.write(str(cnt)+"\n")