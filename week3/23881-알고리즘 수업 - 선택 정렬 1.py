n,k = map(int, input().split())
li = list(map(int, input().split()))
count = 0
answer = -1

for i in range(n-1, 0, -1):
    index = li.index(max(li[:i+1]))
    if index != i:
        li[index], li[i] = li[i], li[index]
        count += 1
        if count == k:
            answer = str(li[index]) + ' ' + str(li[i])
            break
        
print(answer)
