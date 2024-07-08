from collections import defaultdict

def solution(clothes):
    answer = 0
    clothes_dict = defaultdict(int)
    for tp in clothes:
        clothes_dict[tp[1]] += 1
    answer = 1
    for key,val in clothes_dict.items():
        answer *= val+1
    answer -= 1
    
    return answer