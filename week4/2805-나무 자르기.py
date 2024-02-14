import sys
input = sys.stdin.readline

n,m = map(int, input().split())
li = list(map(int, input().split()))
start, end = 1, 1000000000

while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in li:
        if i > mid:
            total += i - mid
    
    if total < m:
        end = mid - 1
    else:
        start = mid + 1
    
print(end)
