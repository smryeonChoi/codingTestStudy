import string
def solution(my_string) :
    ab_list = list(string.ascii_uppercase) + list(string.ascii_lowercase)
    ans = [0 for i in ab_list]
    for i in my_string :
        ans[ab_list.index(i)] += 1
    return ans