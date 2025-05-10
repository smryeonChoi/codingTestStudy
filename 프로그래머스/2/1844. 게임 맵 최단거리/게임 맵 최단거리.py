from collections import deque

def solution(maps) :
    n,m = len(maps),len(maps[0])
    visited = [[0] * m for _ in range(n)]
    queue = deque()
    
    
    # 초기 데이터 삽입
    queue.append((0,0))
    visited[0][0] = 1
    # 방향
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    
    while queue :
        x,y = queue.popleft()
        for dx,dy in directions :
            nx,ny = x+dx,y+dy
            if 0<=nx<n and 0<=ny<m :
                if maps[nx][ny] == 1 and visited[nx][ny] == 0 :
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx,ny))
    return visited[n-1][m-1] if visited[n-1][m-1] != 0 else -1




'''
from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[0] * m for _ in range(n)]
    queue = deque()
    
    # 시작점
    queue.append((0, 0))
    visited[0][0] = 1  # 시작 지점은 거리 1

    # 4방향 이동: 상하좌우
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y = queue.popleft()
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
    
    # 도착지에 도달했는지 확인
    return visited[n-1][m-1] if visited[n-1][m-1] != 0 else -1
    '''