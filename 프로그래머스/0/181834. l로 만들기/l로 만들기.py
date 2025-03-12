# import string
# def solution(myString) :
#     lowers = [i for i in string.ascii_lowercase]
#     for i in myString :
#         if lowers.index(i) < lowers.index('l') :
#             myString = myString.replace(i,'l')
#     return myString

# 풀이 2
def solution(myString) :
    return ''.join([x if x > 'l' else 'l' for x in myString])