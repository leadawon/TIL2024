import sys

N,M = map(int,sys.stdin.readline().split())

limit = [0 for _ in range(100)]

check = [0 for _ in range(100)]

indicator = 0

for i in range(N): 
    length, speed = map(int,sys.stdin.readline().split())
    for j in range(length):
        limit[indicator+j] = speed
    indicator += length
indicator = 0

for i in range(M): 
    length, speed = map(int,sys.stdin.readline().split())
    for j in range(length):
        check[indicator+j] = speed
    indicator += length

delta = 0
for i in range(100):
    if delta < check[i]-limit[i]:
        delta = check[i]-limit[i]
sys.stdout.write(str(delta))
        