import sys
input = sys.stdin.readline


n = int(input())
li = [int(input()) for _ in range(n)]
li = li[::-1]
index = li[0]
cnt = 0

for i in range(1,n):
    if li[i] > index:
        cnt += 1
        index = li[i]

print(cnt+1)
