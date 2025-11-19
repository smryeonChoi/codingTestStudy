from collections import deque 
def diff(a,b) :
    diff = 0
    for i in range(len(a)) :
        if a[i] != b[i] :
            diff += 1
    return diff
def solution(begin,target,words) :
    v = [0]* len(words)
    q = deque([[begin,0]])
    while q :
        c_word,c_dist = q.popleft()
        if c_word == target :
            return c_dist
        for i in range(len(words)) :
            if diff(c_word,words[i]) == 1 and v[i] == 0 :
                q.append([words[i],c_dist+1])
    return 0