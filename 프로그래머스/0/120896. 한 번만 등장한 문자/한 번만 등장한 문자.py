def solution(s) :
    numbers = [s.count(i) for i in s]
    answer = []
    for i in range(len(numbers)) :
        if numbers[i] == 1 :
            answer.append(s[i])
    return ''.join(sorted(answer))