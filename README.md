### 10월 23일

#### 헌내기는 친구가 필요해
```
from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().strip().split())
cam = [ list(input()) for _ in range(N)]
cnt =0

q = deque()
visited = [[0] * M for _ in range(N)]
di = [(0,1), (1, 0), (-1, 0), (0,-1)]

for i in range(N):
    for j in range(M):
        if cam[i][j] == 'I':
            q.append((i,j))# 시작점 설정
            visited[i][j] =1
            break

while q:
    y, x = q.popleft()

    # 주변을 탐색
    for d in di:
        dy, dx = y + d[0], x + d[1]
        # 범위 체크 및 방문하지 않은 곳만 처리
        if 0 <= dy < N and 0 <= dx < M and not visited[dy][dx]:
            visited[dy][dx] = 1  # 방문 표시

            # 장애물이 아닌 경우만 이동
            if cam[dy][dx] != 'X':
                q.append((dy, dx))

                # 사람이 있는 경우 카운트
                if cam[dy][dx] == 'P':
                    cnt += 1

# 결과 출력
if cnt > 0:
    print(cnt)
else:
    print("TT")

```

### 10월 22일

#### 헌내기
```
N, M = map(int, input().split())
cam = [input().split() for _ in range(N)]

queue = []
visited = []

for i in range(N):
    for j in range(M):
        if cam[i][j] == 'I':
            sx, sy = i, j

def bfs(sx,sy):

bfs로 하려니까 모르겠어요 ㅜ

```
#### N과 M(4)
```
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

```

#### N과 M(5)
```
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
```


### 10월 17일 ###

#### N과 M(2) ####

```
N, M = map(int, input().split())
path = []

def dfs(lev, start):
    if lev == M:
        print(*path)
        return

    for i in range(start, N+1):
        if i not in path:
            path.append(i)
            dfs(lev+1, i)
            path.pop()

dfs(0,1)
```
이거푸니까 잠이쏟아져서 포기 gg..
