import sys

W,N = map(int,sys.stdin.readline().split())

arr = []

for i in range(N):
    wei,val = map(int,sys.stdin.readline().split())
    arr.append((wei,val))
arr = sorted(arr,key=lambda x: x[1])

result = 0

while W>0 and len(arr):
    wei,val=arr.pop()
    if W<wei:
       
        result += W*val
        W = 0
    else:
        W -= wei
        result += wei * val
sys.stdout.write(str(result))

## 정렬해서 큰거부터. 그리디?