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
