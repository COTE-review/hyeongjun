t = int(input())
answer = []
 
for _ in range(t):
    n,m = map(int, input().split())
    queue = list(map(int, input().split()))
    pointer, cnt = 0, 0
    
    while True:
        if queue[pointer] >= max(queue):
            if pointer == m:
                break
            cnt += 1
            queue[pointer] = -1
        pointer = (pointer + 1) % n
    answer.append(cnt+1)

print("\n".join(map(str, answer)))