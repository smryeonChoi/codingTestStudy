def solution(numbers) :
    return max([i*k for i in numbers for k in numbers[numbers.index(i)+1:]])