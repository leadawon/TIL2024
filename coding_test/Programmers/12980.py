def make_odd(n):
    while n % 2 == 0:
        n = n//2
    return n

def solution(n):
    ans = 0
    while True:
        if n%2==0:
            n=make_odd(n)
        if n==1:
            ans+=1
            break
        ans+=1
        n-=1
        if n==1:
            ans+=1
            break
        
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return ans