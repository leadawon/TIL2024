import sys
from copy import deepcopy as dc
sys.setrecursionlimit(2000)

N = int(sys.stdin.readline().strip())

arr = list(map(int,sys.stdin.readline().split()))

operator = list(map(int,sys.stdin.readline().split()))

def cpp_div(a,b):
    if a<0:
        return -1 * (-1 * a // b)
    else:
        return a//b

minval = sys.maxsize
maxval = -1 * sys.maxsize
def dfs(operator,arr,val):
    global minval, maxval
    if sum(operator) == 0:
        if val > maxval:
            maxval = val
        if val < minval:
            minval = val
    else:
        
        if operator[0] > 0:
            new_operator = dc(operator)
            new_operator[0] -= 1
            dfs(new_operator, arr[1:], val + arr[0])
        if operator[1] > 0:
            new_operator = dc(operator)
            new_operator[1] -= 1
            dfs(new_operator, arr[1:], val - arr[0])
        if operator[2] > 0:
            new_operator = dc(operator)
            new_operator[2] -= 1
            dfs(new_operator, arr[1:], val * arr[0])
        if operator[3] > 0:
            new_operator = dc(operator)
            new_operator[3] -= 1
            dfs(new_operator, arr[1:], cpp_div(val , arr[0]))

dfs(operator,arr[1:],arr[0])
sys.stdout.write(f"{maxval}\n{minval}")