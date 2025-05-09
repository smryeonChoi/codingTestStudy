def solution(par,com) :
    temp = 0
    dic = {}
    for p in par :
        dic[hash(p)] = p
        temp += hash(p)
    for c in com :
        temp -= hash(c)
    return dic[temp]