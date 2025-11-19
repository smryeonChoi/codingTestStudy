def solution(maps) :
    n,m = len(maps),len(maps[0])
    v = [[0]*m for _ in range(n)]
    def bfs(si,sj,ei,ej) :
        q = []
        q.append((si,sj))
        v[si][sj] = 1
        while q :
            ci,cj = q.pop(0)
            if ci == ei and cj == ej :
                return v[ci][cj]
            for di,dj in [(-1,0),(1,0),(0,-1),(0,1)] :
                ni,nj = ci+di, cj+dj
                if 0<=ni<n and 0<=nj<m and maps[ni][nj] == 1 and v[ni][nj] == 0 :
                    q.append((ni,nj))
                    v[ni][nj] = v[ci][cj] + 1
        return -1
    return bfs(0,0,n-1,m-1)