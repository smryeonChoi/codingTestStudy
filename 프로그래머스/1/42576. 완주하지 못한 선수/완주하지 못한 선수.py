from collections import Counter 

def solution(par,com) :
    p = Counter(par)
    c = Counter(com) 
    diff = p-c
    return list(diff.keys())[0]