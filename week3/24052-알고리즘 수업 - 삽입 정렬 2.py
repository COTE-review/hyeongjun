import sys
input = sys.stdin.readline

n,k = map(int, input().split())
li = list(map(int, input().split()))

def insertion_sort(li):
    cnt = 0
    for i in range(1,len(li)):
        loc = i - 1
        newItem = li[i]

        while 0 <= loc and newItem < li[loc]:
            li[loc + 1] = li[loc]
            loc -= 1
            cnt += 1
            if cnt == k:
                return True
        
        if loc + 1 != i:
            li[loc + 1] = newItem
            cnt += 1
            if cnt == k:
                return True
    return False
            
answer = insertion_sort(li)
print(" ".join(map(str, li)) if answer else -1) 