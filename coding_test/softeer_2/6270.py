# import sys

# N,M = map(int,sys.stdin.readline().split())

# limit = [0 for _ in range(100)]

# check = [0 for _ in range(100)]

# indicator = 0

# for i in range(N): 
#     length, speed = map(int,sys.stdin.readline().split())
#     for j in range(length):
#         limit[indicator+j] = speed
#     indicator += length
# indicator = 0

# for i in range(M): 
#     length, speed = map(int,sys.stdin.readline().split())
#     for j in range(length):
#         check[indicator+j] = speed
#     indicator += length

# delta = 0
# for i in range(100):
#     if delta < check[i]-limit[i]:
#         delta = check[i]-limit[i]
# sys.stdout.write(str(delta))
import sys
N,M = map(int,sys.stdin.readline().split())
narr = []
marr = []
cp=set()
for i in range(N):
    leng,velo = map(int,sys.stdin.readline().split())
    cp.add(len(narr)+leng)
    for j in range(leng):
        narr.append(velo)
for i in range(M):
    leng,velo = map(int,sys.stdin.readline().split())
    cp.add(len(marr)+leng)
    for j in range(leng):
        marr.append(velo)
max_delta = 0
for i in cp:
    max_delta = max(max_delta,marr[i-1]-narr[i-1])
    
sys.stdout.write(str(max_delta))