
def solution(n,computers) :
    visited = [0] * n
    answer = 0
    
    def dfs(c) :
        visited[c] = 1
        for next in range(n) :
            if computers[c][next] == 1 and visited[next] == 0 :
                dfs(next)
    for i in range(n) :
        if not visited[i] :
            dfs(i)
            answer += 1
    return answer

'''
def solution(n,computers) :
    visited = [0] * n
    def dfs(c) :
        visited[c] = 1
        for next in range(n) :
            if computers[c][next] == 1 and visited[next] == 0 :
                dfs(next)
    count = 0
    for i in range(n) :
        if not visited[i] :
            dfs(i)
            count += 1 
    return count'''

