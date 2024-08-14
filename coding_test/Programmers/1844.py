from collections import deque
from copy import deepcopy
def solution(maps):
    answer = -1
    maps[0][0] = 0
    maps[-1][-1] = 2
    n = len(maps)
    m = len(maps[0])
    dq = deque() 
    dq.append([maps,0,0,1])
    # maps, now row, now col , ans
    
    while dq:
        maps,row,col,ans=dq.popleft()
        
        if row > 0 and maps[row-1][col] != 0:
            if row-1==n-1 and col==m-1:
                return ans+1
            
            maps[row-1][col] = 0
            dq.append([maps,row-1,col,ans+1])
        if col < m-1 and maps[row][col+1] != 0:
            if row==n-1 and col+1==m-1:
                return ans+1
            
            maps[row][col+1] = 0
            dq.append([maps,row,col+1,ans+1])
        if row < n-1 and maps[row+1][col] != 0:
            if row+1==n-1 and col==m-1:
                return ans+1
            
            maps[row+1][col] = 0
            dq.append([maps,row+1,col,ans+1])
        if col > 0 and maps[row][col-1] != 0:
            if row==n-1 and col-1==m-1:
                return ans+1
            maps[row][col-1] = 0
            dq.append([maps,row,col-1,ans+1])
        
        
        
            
    
    
    return answer