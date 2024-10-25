import sys
input = sys.stdin.readline

from collections import deque

def bfs(y,x):
    global cnt
    q = deque()
    q.append((1, y, x))
    visited[y][x] = 1

    while q:
        move, dy, dx = q.popleft()

        if dy == N-1 and dx == M-1:
            cnt = min(cnt, move)
            break

        for d in di:
            ny, nx = dy + d[0], dx + d[1]
            if 0 <= ny < N and 0 <= nx < M and arr[ny][nx] == 1 and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                q.append((move+1, ny, nx))

di = [(1,0),(0,1),(-1,0),(0,-1)]
N, M = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
cnt = float('inf')
bfs(0, 0)

print(cnt)

'''
1. 우리가 무슨 로직으로 문제를 풀지 일단 생각먼저
여기에서는 보장되어있는게 무엇이지?
시작위치 종료위치
그리고 입력은 어떻게 받지?
세로 가로 길이랑 배열
근데 최소 이동 횟수라는게 문제에서 나옴 => bfs
queue를쓴다.
'''




