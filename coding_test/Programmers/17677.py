from collections import defaultdict


def checkalphabet2(c1,c2):
    return checkalphabet1(c1) , checkalphabet1(c2)

def checkalphabet1(onechar):
    if ord(onechar) >= ord('a') and ord(onechar) <= ord('z'):
        return ord(onechar) + (ord('A')-ord('a'))
    elif ord(onechar) >= ord('A') and ord(onechar) <= ord('Z'):
        return ord(onechar)
    return 0

def getdict(str1,dd1):
    prestr = str1[0]
    
    for s in str1[1:]:
        
        former,latter = checkalphabet2(prestr,s)
        if former and latter:
            
            dd1[chr(former)+chr(latter)] += 1
        prestr = s
    
def getscore(dd1,dd2):
    iscore = 0
    uscore = 0
    for k,v in dd1.items():
        iscore += min(v,dd2[k])
        uscore += v
    
    for k,v in dd2.items():
        uscore += v
    uscore -= iscore
    print(iscore,uscore)
    return int(iscore/uscore * 65536)
        
    
    
def solution(str1, str2):
    
    answer = 65536
    dd1 = defaultdict(int)
    dd2 = defaultdict(int)
    getdict(str1,dd1)
    getdict(str2,dd2)
    
    if dd1 or dd2:
        answer = getscore(dd1,dd2)
    
    
    return answer