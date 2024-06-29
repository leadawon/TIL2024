import sys

# 외우기용
sys.setrecursionlimit(5000)

N,M = map(int, sys.stdin.readline().split())

room_dict = dict()


for i in range(N):
    room_dict[sys.stdin.readline().strip()] = [0 for _ in range(9)]
    
for i in range(M):
    a,b,c = sys.stdin.readline().split()
    for j in range(int(b),int(c)):
        room_dict[a][j-9] = 1

result = []

for k,v in room_dict.items():
    empty_time = []
    last0 = False
    start_idx = 0
    for j in range(9):
        if v[j] == 1 and last0:
            empty_time.append(str(start_idx+9).zfill(2) + "-" + str(j+9))
            last0 = False
        elif v[j] == 1 and not last0:
            continue
        elif v[j] == 0 and last0:
            continue
        else:
            start_idx = j
            last0 = True
    else:
        if last0:
            empty_time.append(str(start_idx+9).zfill(2) + "-18")
    result.append((k,len(empty_time),empty_time))

result = sorted(result,key=lambda x:x[0])

for idx,tp in enumerate(result):
    if tp[1] == 0:
        sys.stdout.write("Room " + tp[0] + ":\nNot available\n")
    else:
        sys.stdout.write("Room " + tp[0] + ":\n"+str(tp[1])+" available:\n")
        for time in tp[2]:
            sys.stdout.write(time+"\n")
    if idx<len(result)-1:
        sys.stdout.write("-----\n")
    
            
            
            


    