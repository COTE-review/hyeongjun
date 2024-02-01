import sys
input = sys.stdin.readline


def binary_search(li, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if li[mid] == target:
            return 1
        elif li[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0


n = int(input())
number_list = sorted(list(map(int,input().split())))
m = int(input())
check_list = list(map(int,input().split()))

for check in check_list:
    print(binary_search(number_list, check, 0, n-1))
