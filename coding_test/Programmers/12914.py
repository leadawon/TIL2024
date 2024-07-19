from itertools import combinations as cb
import math
def solution(n):
    answer = 0
    for i in range(n//2+1):
        #answer+=len(list(cb(range(n-i),i)))
        answer= (answer+math.comb(n-i,i))%1234567
    return answer