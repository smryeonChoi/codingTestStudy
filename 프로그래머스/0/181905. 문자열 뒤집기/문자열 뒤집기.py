def solution(my_string,s,e) :
    ans = my_string[s:e+1]
    return my_string[:s]+ans[::-1]+my_string[e+1:]