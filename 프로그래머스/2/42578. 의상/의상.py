'''
def solution(clothes):
    dic = {}
    for cloth, type in clothes:
        if type not in dic:
            dic[type] = 0
        dic[type] += 1
    result = 1
    for _,value in dic.items() :
        result *= (value + 1)
    return result - 1
'''
def solution(clothes) :
    closet = {}
    for x,y in clothes :
        if y not in list(closet.keys()) :
            closet[y] = 0
        closet[y] += 1
    result = 1
    for i in list(closet.values()) :
        result *= (i+1)
    return result - 1