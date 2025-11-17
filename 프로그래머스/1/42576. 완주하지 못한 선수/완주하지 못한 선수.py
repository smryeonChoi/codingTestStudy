def solution(par,com) :
    hash_table = {}
    temp = 0
    for p in par :
        hash_table[hash(p)] = p
        temp += hash(p)
    for c in com :
        temp -= hash(c)
    return hash_table[temp]