def solution(numbers,target) :
    bfs = [0]
    for i in numbers :
        temp = []
        for j in bfs :
            temp.append(j+i)
            temp.append(j-i)
        bfs = temp
    return bfs.count(target)