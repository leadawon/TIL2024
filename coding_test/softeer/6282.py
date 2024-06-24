import sys
sys.setrecursionlimit(5000)
N=int(sys.stdin.readline().strip())

arr = [[0 for _ in range(N)] for _ in range(N)]

for row_idx in range(N):
    one_row = sys.stdin.readline().strip()
    for col_idx,col_val in enumerate(one_row):
        arr[row_idx][col_idx] = int(col_val)

def dfs(row_now,col_now,arr,unique):
    arr[row_now][col_now] = unique
    global cnt
    cnt += 1
    if row_now!=0 and arr[row_now-1][col_now]==1:
        dfs(row_now-1,col_now,arr,unique)
    if col_now!=N-1 and arr[row_now][col_now+1]==1:
        dfs(row_now, col_now+1,arr,unique)
    if row_now!=N-1 and arr[row_now+1][col_now]==1:
        dfs(row_now+1,col_now,arr,unique)
    if col_now!=0 and arr[row_now][col_now-1]==1:
        dfs(row_now,col_now-1,arr,unique)
    
        

unique = 2
result_arr = []
for row_idx in range(N):
    for col_idx in range(N):
        if arr[row_idx][col_idx] == 1:
            cnt = 0
            dfs(row_idx,col_idx,arr,unique)
            result_arr.append(cnt)
            unique+=1
sys.stdout.write(str(unique-2)+"\n")
for val in sorted(result_arr):
    sys.stdout.write(str(val)+"\n")
            