# 내 풀이
# def solution(my_string) :
#     for i in my_string :
#         if not i.isdigit() :
#             my_string = my_string.replace(i, ' ')
#     answer = 0
#     for i in my_string.split(' ') :
#         if i.isdigit() :
#             answer += int(i)
#     return answer

# 좀 더 간단한 풀이
def solution(my_string) :
    s = ''.join(i if i.isdigit() else ' ' for i in my_string )
    return sum(int(i) for i in s.split())
    