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










