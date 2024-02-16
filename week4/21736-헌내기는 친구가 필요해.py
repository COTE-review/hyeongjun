from collections import deque

n, m = map(int,input().split())
board = [list(input()) for _ in range(n)]

dr = [0,0,-1,1]
dc = [-1,1,0,0]

def bfs(r,c):
    friend = 0
    queue = deque()
    queue.append((r,c))
    while queue:
        r,c = queue.popleft()
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if board[nr][nc] == 'P':
                    friend += 1
                    queue.append((nr,nc))
                    board[nr][nc] = 'X'
                elif board[nr][nc] == 'O':
                    queue.append((nr,nc))
                    board[nr][nc] = 'X'

    return friend


for r in range(n):
    for c in range(m):
        if board[r][c] == 'I':
            answer = bfs(r,c)

print(answer if answer > 0 else 'TT')
