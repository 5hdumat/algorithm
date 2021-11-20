'''
7
1 1 0 0 0 1 0
0 1 1 0 1 1 0
0 1 0 0 0 0 0
0 0 0 1 0 1 1
1 1 0 1 1 0 0
1 0 0 0 1 0 0
1 0 1 0 1 0 0
'''
from collections import deque

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

Q = deque()
cnt = 0

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            cnt += 1
            board[i][j] = 0
            Q.append((i, j))

            while Q:
                tmp = Q.popleft()

                for k in range(8):
                    x = tmp[0] + dx[k]
                    y = tmp[1] + dy[k]
                    if 0 <= x < n and 0 <= y < n and board[x][y] == 1:
                        board[x][y] = 0
                        Q.append((x, y))

print(cnt)
