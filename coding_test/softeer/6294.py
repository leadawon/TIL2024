import sys

sys.setrecursionlimit(1000)

number = 10
f"{number:.2f}"

N,K = map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))

dp_arr = []
temp = 0
for score in arr:
    temp += score
    dp_arr.append(temp)
# 10 60 80 150 250
for i in range(K):
    s,e = map(int,sys.stdin.readline().split())
    if s==1:
        sys.stdout.write(f"{round(dp_arr[e-1]/e,2):.2f}\n")
    else:
        sys.stdout.write(f"{round((dp_arr[e-1]-dp_arr[s-2])/(e-s+1),2):.2f}\n")
    