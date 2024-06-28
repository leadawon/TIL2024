import sys

arr = [[0 for _ in range(3)] for _ in range(3)]

for i in range(3):
    arr[i][0],arr[i][1],arr[i][2] = map(int,sys.stdin.readline().split())

min_delta = 99

for i in range(3):#가로로 3번
    sorted_arr = sorted(arr[i])
    if min_delta > sorted_arr[2] - sorted_arr[0]:
        min_delta = sorted_arr[2] - sorted_arr[0]
        
for i in range(3):#세로로 3번
    new_arr = [arr[j][i] for j in range(3)]
    sorted_arr = sorted(new_arr)
    if min_delta > sorted_arr[2] - sorted_arr[0]:
        min_delta = sorted_arr[2] - sorted_arr[0]
sys.stdout.write(str(min_delta))
        