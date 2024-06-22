import sys

arr = list(map(int, sys.stdin.readline().split()))
cnt = arr[0]

if cnt<arr[1]:
    for i in arr:
        if cnt==i:
            cnt+=1
        else:
            sys.stdout.write("mixed")
            break
    else:
        sys.stdout.write("ascending")
else:
    for i in arr:
        if cnt==i:
            cnt-=1
        else:
            sys.stdout.write("mixed")
            break
    else:
        sys.stdout.write("descending")
