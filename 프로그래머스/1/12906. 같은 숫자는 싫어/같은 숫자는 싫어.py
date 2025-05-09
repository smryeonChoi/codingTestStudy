def solution(arr) :
    ans = [arr[0]]
    for i in arr[1:] :
        if i != ans[-1] :
            ans.append(i)
    return ans






'''
def solution(arr) :
    ans = [arr[0]]
    for i in arr[1:] :
        if i != ans[-1] :
            ans.append(i)
    return ans'''