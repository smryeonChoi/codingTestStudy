def solution(citations) :
    citations.sort(reverse = True)
    for i in range(len(citations)) :
        if citations[i] < i + 1 :
            return i
    return len(citations)




'''
def solution(citations) :
    citations.sort(reverse=True)
    for idx,value in enumerate(citations) :
        if idx + 1 > value :
            return idx
    return len(citations)
'''