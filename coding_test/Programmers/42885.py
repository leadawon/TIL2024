from collections import deque

def solution(people, limit):
    answer = 0
    people = deque(sorted(people))
    while len(people) > 1:
        left = limit-people[-1]
        people.pop()
        if left >= people[0]:
            people.popleft()
        answer+=1
    if people:
        answer+=1
    return answer