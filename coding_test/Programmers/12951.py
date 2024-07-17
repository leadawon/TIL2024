def solution(s):
    answer = '' # 97 65
    blank = []
    flag = True
    cnt = 0
    for i in s:
        
        if i==" ":
            cnt += 1
            flag = True
        elif flag:
            flag = False
            blank.append(cnt)
            cnt = 0
    
    blank.append(cnt)

    arr = list(s.split())
    for i,v in enumerate(arr):
        temp = []
        temp.append(" "*blank[i])
        if ord(v[0]) >= ord('a') and ord(v[0]) <= ord('z'):
            temp.append(chr(ord(v[0])-32))
        else:
            temp.append(v[0])
        for j in range(1,len(v)):
            if ord(v[j]) >= ord('A') and ord(v[j]) <= ord('Z'):
                temp.append(chr(ord(v[j])+32))
            else:
                temp.append(v[j])
        
        arr[i] = "".join(temp)
    arr.append(" "*blank[-1])
    answer = "".join(arr)
    return answer