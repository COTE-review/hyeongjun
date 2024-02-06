import sys
input = sys.stdin.readline

n,k = map(int, input().split())
li = list(map(int, input().split()))
answer = -1

for i in range(n-1, 0, -1):
    for j in range(i):
        if li[j] > li[j+1]:
            li[j], li[j+1] = li[j+1], li[j]
            k -= 1
            if k == 0:
                answer = str(li[j]) + ' ' + str(li[j+1])
                break

print(answer)
