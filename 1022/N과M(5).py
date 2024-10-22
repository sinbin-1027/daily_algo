import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
arr = list(map(int, input().split()))

arr.sort()
path = []

def dfs(lev):
    if lev == M:
        print(*path)
        return

    for i in arr:
        if i not in path:
            path.append(i)
            dfs(lev+1)
            path.pop()

dfs(0)



