def check_pair(a,b):
    if a=="{" and b=="}" or a=="[" and b=="]" or a=="(" and b==")":
        return True
    return False
        

def check_list(tgs):
    stack = [tgs[0]]
    for val in tgs[1:]:
        
        if stack and check_pair(stack[-1],val):
            stack.pop()
        else:
            stack.append(val)
    if stack:
        return False
    return True


def solution(s):
    answer = 0
    temp_str = ""
    for shift in range(len(s)):
        temp_str = s[shift:]+s[:shift]
        if check_list(temp_str):
            answer+=1
        
        
    return answer