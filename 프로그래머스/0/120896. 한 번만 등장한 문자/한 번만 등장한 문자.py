#  풀이1
# def solution(s) :
#     numbers = [s.count(i) for i in s]
#     answer = []
#     for i in range(len(numbers)) :
#         if numbers[i] == 1 :
#             answer.append(s[i])
#     return ''.join(sorted(answer))

# 풀이2
def solution(s) : 
    answer = ''.join(sorted([ch for ch in s if s.count(ch) == 1]))
    return answer