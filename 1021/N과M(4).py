import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
path = []
v = []

def dfs(lev,num):
    if lev == M: # 길이가 M이면 가지치기
        print(*path)
        return

    for i in range(num, N+1): # num부터 시작, num보다 작은 수가 들어가면 중복
        path.append(i)
        dfs(lev+1, i) # i가 기준.
        path.pop()

dfs(0,1)