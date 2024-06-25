import sys

M,N,K = map(int,sys.stdin.readline().split())

secret_arr = list(map(int,sys.stdin.readline().split()))

user_arr = list(map(int,sys.stdin.readline().split()))

flag = False
for user_idx in range(len(user_arr)-len(secret_arr)+1):
    if flag:
        break
    for secret_idx in range(len(secret_arr)):
        if secret_arr[secret_idx] != user_arr[user_idx+secret_idx]:
            break
    else:
        flag = True
if flag:
    sys.stdout.write("secret")
else:
    sys.stdout.write("normal")