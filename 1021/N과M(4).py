import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
path = []
v = []

def dfs(lev):
    if lev == M:
        print(*path)
        return

    for i in range(1, N+1):
        path.append(i)
        dfs(lev+1)
        path.pop()

dfs(0)