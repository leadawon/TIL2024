import sys
sys.setrecursionlimit(50000)

def dfs_recursion(arr,cursor,mem_num,tg_num):
    global answer
    if cursor > len(arr)-1:
        if mem_num == tg_num:
            answer += 1
    else:
        dfs_recursion(arr,cursor+1,mem_num+arr[cursor],tg_num)
        dfs_recursion(arr,cursor+1,mem_num-arr[cursor],tg_num)
    
def dfs_stack(arr,tg_num):
    answer=0
    stack_dfs = [(0,0)] # cursor, mem
    while stack_dfs:
        tp=stack_dfs.pop()
        if tp[0] > len(arr) -1:
            if tp[1] == tg_num:
                answer += 1
        else:
            stack_dfs.append((tp[0]+1,tp[1]+arr[tp[0]]))
            stack_dfs.append((tp[0]+1,tp[1]-arr[tp[0]]))
    return answer
    
    

def solution(numbers, target):
    global answer
    answer = 0
    dfs_recursion(numbers,0,0,target)
    answer = dfs_stack(numbers,target)
    
    
    return answer