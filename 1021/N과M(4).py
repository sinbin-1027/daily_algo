import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
path = []
v = []

def dfs(lev,num):
    if lev == M:
        print(*path)
        return

    for i in range(num, N+1):
        path.append(i)
        dfs(lev+1, i)
        path.pop()

dfs(0,1)