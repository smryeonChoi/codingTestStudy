def solution(a,b,c) :
    ans = len(set([a,b,c]))
    if ans == 1:
        return (3*a)*3*(a**2)*3*(a**3)
    elif ans == 2 :
        return (a+b+c) * (a **2 + b**2 + c**2)
    else :
        return a + b + c