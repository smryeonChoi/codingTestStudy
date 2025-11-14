def solution(priorities,location) : 
    prior = [(i,p) for i,p in enumerate(priorities)]
    ans = 0
    while True :
        cur = prior.pop(0)
        if any(cur[1] < p[1] for p in prior) :
            prior.append(cur)
        else :
            ans += 1
            if cur[0] == location :
                return ans
    