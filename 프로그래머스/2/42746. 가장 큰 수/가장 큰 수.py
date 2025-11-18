def solution(numbers) :
    max_len = len(str(max(numbers)))
    arr = sorted([str(n) for n in numbers],key = lambda x : str(x) * max_len, reverse = True)
    ans = ''.join(arr)
    return ans if int(ans) != 0 else '0'





'''
def solution(numbers) :
    # 세자리까지 만들수 있기 때문에
    numbers = sorted([str(i) for i in numbers],key = lambda x : str(x) * 3 ,reverse=True)
    result = ''.join(numbers)
    return result if int(result) != 0 else '0'
'''


