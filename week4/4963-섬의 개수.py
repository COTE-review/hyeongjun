import sys
from collections import deque
input = sys.stdin.readline

dx = [1,-1,0,0,1,-1,1,-1]
dy = [0,0,-1,1,-1,1,1,-1]

def bfs(r,c):
    field[r][c] = 0
    queue = deque()
    queue.append([r,c])
    while queue:
        r,c = queue.popleft()
        for i in range(8):
            nx = r + dx[i]
            ny = c + dy[i]
            if 0 <= nx < h and 0 <= ny < w and field[nx][ny] == 1:
                field[nx][ny] = 0
                queue.append([nx,ny])

while True:
    w,h = map(int,input().split())
    if w == 0 and h == 0:
        break
    field = []
    cnt = 0

    for _ in range(h):
        field.append(list(map(int, input().split())))

    for r in range(h):
        for c in range(w):
            if field[r][c] == 1:
                bfs(r,c)
                cnt += 1
    print(cnt)
