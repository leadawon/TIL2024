import sys

sys.setrecursionlimit(1000)

N,M,V = map(int,sys.stdin.readline().split())

arr = [[] for i in range(N)]


for i in range(M):
    s,e = map(int,sys.stdin.readline().split())
    arr[s-1].append(e-1)
    arr[e-1].append(s-1)

start_idx = V-1
for i in range(N):
    arr[i] = sorted(arr[i])

def dfs(arr,visited,tg,traverse):
    visited[tg] = True
    traverse.append(tg)
    for new_tg in arr[tg]:
        if visited[new_tg]:
            continue
        else:
            dfs(arr,visited,new_tg,traverse)

from collections import deque

def bfs(arr, visited, tg, traverse):
    queue = deque([tg])
    visited[tg] = True
    
    while queue:
        node = queue.popleft()
        traverse.append(node)
        for new_tg in arr[node]:
            if not visited[new_tg]:
                queue.append(new_tg)
                visited[new_tg] = True


visited = [False for _ in range(N)]
traverse = []

dfs(arr,visited,start_idx,traverse)

for i in traverse:
    sys.stdout.write(str(i+1)+" ")
sys.stdout.write("\n")

visited = [False for _ in range(N)]
traverse = []

bfs(arr,visited,start_idx,traverse)

for i in traverse:
    sys.stdout.write(str(i+1)+" ")
sys.stdout.write("\n")


    
    