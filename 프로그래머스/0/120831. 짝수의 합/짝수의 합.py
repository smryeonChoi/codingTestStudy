def solution(n) :
    a = [x for x in range(1,n+1) if x % 2 == 0]
    return sum(a)