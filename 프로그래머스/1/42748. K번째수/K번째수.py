def solution(array,com) :
    ans = []
    for c in com :
        arr = sorted(array[c[0]-1:c[1]])
        ans.append(arr[c[2]-1])
    return ans
        



'''
def solution(array,commands) :
    answer = []
    for i,j,k in commands :
        answer.append(sorted(array[i-1:j])[k-1])
    return answer 
'''

