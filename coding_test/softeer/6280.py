import sys

#2,3,5,9

#1,2,4,8

N = int(sys.stdin.readline().strip())

tg=2
delta = 1

for i in range(N):
    tg+=delta
    delta*=2
sys.stdout.write(str(tg*tg))