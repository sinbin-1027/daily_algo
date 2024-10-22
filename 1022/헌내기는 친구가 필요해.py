N, M = map(int, input().split())
cam = [input().split() for _ in range(N)]

queue = []
visited = []

for i in range(N):
    for j in range(M):
        if cam[i][j] == 'I':
            sx, sy = i, j

def bfs(sx,sy):
