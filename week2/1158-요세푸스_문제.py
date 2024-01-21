n,k = map(int, input().split())
people = list(range(1,n+1))
pivot = k - 1
answer = []

for _ in range(n-1):
    answer.append(people[pivot])
    del people[pivot]
    pivot = (pivot + k - 1) % len(people)

answer.append(people[0])
print("<" + ", ".join(map(str,answer)) + ">")
    