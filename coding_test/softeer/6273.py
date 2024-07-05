import sys

sys.setrecursionlimit(1000)

from itertools import permutations as pm
from itertools import combinations as cm
arr = [(1,2),(2,3)]
arr = sorted(arr,key=lambda x:(x[0],-x[1]))
arr = [1,2,2,3]
arr = sorted(arr,key=lambda x:x)


arr = []
N,M,K = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

all_arr = pm(arr)
min_val = M*K
for tp in all_arr:
    bucket = [0 for _ in range(K)]
    tp_idx=0
    for b_idx in range(len(bucket)):
        while(bucket[b_idx] + tp[tp_idx] <= M):
            bucket[b_idx] += tp[tp_idx]
            tp_idx = (tp_idx+1)%N
    if min_val > sum(bucket):
        min_val = sum(bucket)


sys.stdout.write(f"{min_val}")   