# https://atcoder.jp/contests/joi2012yo/tasks/joi2012yo_e
# https://kakedashi-engineer.appspot.com/2020/06/06/joi2012yoe/
W, H = map(int, input().split())
M = [[0]*(W+2)]
for _ in range(H):
    M.append([0] + [int(i) for i in input().split()] + [0])

# y座標が奇数の時
even = [[-1, 0], [1, -1], [0, 1], [-1, -1], [1, 0], [0, -1]]
# y座標が偶数の時
odd = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [0, -1]]


M.append([0]*(W+2))
for m in M:
    print(m)

q = [[0, 0]]
visited = [[False for _ in range(W+2)] for _ in range(H+2)]

cnt = 0
while q:
    y, x = q.pop(0)
    if visited[y][x]:
        continue
    if y % 2 == 0:
        direction = even
    else:
        direction = odd
    visited[y][x] = True
    for dy, dx in direction:
        ny = y+dy
        nx = x+dx
        # ギリギリのインデックスは H+1とW+1であるため
        if 0 <= ny < H+2 and 0 <= nx < W+2:
            if M[ny][nx]:
                cnt += 1
            else:
                q.append([ny, nx])
print(cnt)
