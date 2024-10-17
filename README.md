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
