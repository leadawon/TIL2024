import sys

n = int(sys.stdin.readline().strip())
sum_arr_score = [0 for _ in range(3001)]
sum_arr_user = [0 for _ in range(n)]
for T in range(3):
    contest = list(map(int, sys.stdin.readline().strip().split()))
    
    arr = [0 for _ in range(1001)]
    
    
    
    for idx,val in enumerate(contest):
        
        arr[val]+=1
        sum_arr_user[idx]+=val
    
    ans=[]
    for val in contest:
        cnt = 0
        for j in range(1000-val):
            cnt+=arr[1000-j]
        ans.append(str(cnt+1))

    sys.stdout.write(" ".join(ans)+"\n")

for idx,val in enumerate(sum_arr_user):
        sum_arr_score[val]+=1

ans=[]
    
for i in sum_arr_user:
    cnt = 0
    for j in range(3000-i):
        cnt+=sum_arr_score[3000-j]
    ans.append(str(cnt+1))
sys.stdout.write(" ".join(ans)+"\n")
    
    

## 계수정렬로 해결한다.