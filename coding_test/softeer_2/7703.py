# import sys
# ### 32 빼면 대문자 된다.
# # A-Z 65-90
# # a-z 97-122

# N = int(sys.stdin.readline().strip())
# arr = []
# for _ in range(N):
#     S,T = sys.stdin.readline().split()
#     for idx,val in enumerate(S):
#         if val=='x' or val=='X':
#             if ord(T[idx])>=97 and ord(T[idx])<=122:
#                 arr.append(chr(ord(T[idx])-32))
#             else:
#                 arr.append(T[idx])
#             break
# sys.stdout.write("".join(arr))





import sys

N = int(sys.stdin.readline().strip())

for i in range(N):
    first, second = sys.stdin.readline().split()
    xloc = 0
    for jidx,jval in enumerate(first):
        if jval == 'X' or jval == 'x':
            xloc = jidx
            break
    if ord(second[xloc]) >= ord('a') and ord(second[xloc]) <= ord('z'):
        sys.stdout.write(chr(ord(second[xloc])-32))
    else:
        sys.stdout.write(second[xloc])


