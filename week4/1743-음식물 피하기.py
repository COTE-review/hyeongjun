from collections import deque

n, m, v = map(int, input().split())
board = [['.'] * m for _ in range(n)] 

for _ in range(v):
    a,b = map(int, input().split())
    board[a-1][b-1] = '#'

dr = [0,0,-1,1]
dc = [-1,1,0,0]

def bfs(r,c):
    cnt = 1
    queue = deque()
    queue.append([r,c])
    board[r][c] = '.'
    while queue:
        r,c = queue.popleft()
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0 <= nr < n and 0 <= nc < m and board[nr][nc] == '#':
                cnt += 1
                queue.append([nr,nc])
                board[nr][nc] = '.'
    return cnt

rubbish = []
for r in range(n):
    for c in range(m):
        if board[r][c] == '#':
            rubbish.append(bfs(r,c))

print(max(rubbish))
