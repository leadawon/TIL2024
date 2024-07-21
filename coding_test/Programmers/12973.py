def solution(s):
    answer = -1
    stack = [s[0]]
    for c in s[1:]:
        if len(stack) and stack[-1] == c:
            stack.pop()
            continue
        else:
            stack.append(c)
    if len(stack):
        answer = 0
    else:
        answer = 1
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer