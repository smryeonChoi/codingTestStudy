def solution(citations) :
    citations.sort(reverse = True)
    ans = 0
    for i in range(len(citations)) :
        if citations[i] >= i + 1 :
            ans += 1
    return ans




'''
def solution(citations) :
    citations.sort(reverse=True)
    for idx,value in enumerate(citations) :
        if idx + 1 > value :
            return idx
    return len(citations)
'''