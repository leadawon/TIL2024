# import sys

# N = int(sys.stdin.readline().strip())

# arr = list(map(int,sys.stdin.readline().split()))

# max_val = 0

# for i in range(2,max(arr)+1):
#     cnt = 0
#     for yt in arr:
#         if yt%i==0:
#             cnt += 1
    
#     if max_val < cnt:
#         max_val = cnt

# sys.stdout.write(str(max_val))

import sys

n = int(sys.stdin.readline().strip())

arr = list(map(int,sys.stdin.readline().split()))

max_cnt = 0

for i in range(2,max(arr)+1):
    cnt = 0
    for j in arr:
        if j%i == 0:
            cnt += 1
    if cnt > max_cnt:
        max_cnt = cnt
sys.stdout.write(str(max_cnt))
