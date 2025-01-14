import string
def solution(my_string) :
    answer = []
    for i in my_string :
        if i not in list(string.ascii_lowercase) :
            answer.append(int(i))
    return sorted(answer)