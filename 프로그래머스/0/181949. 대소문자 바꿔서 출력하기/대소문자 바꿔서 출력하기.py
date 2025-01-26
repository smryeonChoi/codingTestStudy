# 풀이1
# str = input()
# strs = list(str)
# for i in range(len(strs)) :
#     if strs[i].isupper() :
#         strs[i] = strs[i].lower()
#     else :
#        strs[i] = strs[i].upper()
# print(''.join(strs))
# 풀이2
print(''.join(x.upper() if x == x.lower() else x.lower() for x in input()))