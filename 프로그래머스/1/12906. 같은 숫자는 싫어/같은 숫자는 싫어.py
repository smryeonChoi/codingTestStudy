
def solution(arr) :
    s = []
    if s == [] :
        s.append(arr[0])
    for i in range(1,len(arr)) :
        if arr[i] != s[-1] :
            s.append(arr[i])
    return s



'''
def solution(arr) :
    ans = [arr[0]]
    for i in arr[1:] :
        if i != ans[-1] :
            ans.append(i)
    return ans'''