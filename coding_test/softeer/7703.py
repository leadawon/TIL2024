import sys
### 32 빼면 대문자 된다.
# A-Z 65-90
# a-z 97-122

N = int(sys.stdin.readline().strip())
arr = []
for _ in range(N):
    S,T = sys.stdin.readline().split()
    for idx,val in enumerate(S):
        if val=='x' or val=='X':
            if ord(T[idx])>=97 and ord(T[idx])<=122:
                arr.append(chr(ord(T[idx])-32))
            else:
                arr.append(T[idx])
            break
sys.stdout.write("".join(arr))