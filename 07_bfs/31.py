# https://atcoder.jp/contests/joi2012yo/tasks/joi2012yo_e
# マップの周囲にパディングを用意して、周りから建物があるかを見ていく、
# そうすると建物の壁にぶつかった時にイルミネーションを施せる回数をカウントしていくことができる。

W, H = map(int, input().split())

# マップの作成
map_ = []
for _ in range(H):
    # 最初と最後に0を追加するのは移動可否判定のため
    map_.append([0] + [int(i) for i in input().split()] + [0])

# 最初と最後に0だけの行を追加する
map_.insert(0, [0] * (W + 2))
map_.append([0] * (W + 2))

# 6角形なので6方向に移動する。ただしmap_は0-indexedなので問題文とは奇数偶数が逆になる
# y座標が偶数の時の移動方向
even = [[-1, 0], [1, -1], [0, 1], [-1, -1], [1, 0], [0, -1]]
# y座標が奇数の時の移動方向
odd = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [0, -1]]

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
            # 建物の壁にぶつかった場合はカウントしてその方向は終了
            if map_[ny][nx]:
                cnt += 1
            # 建物がない場合は次のマスに進む
            else:
                q.append([ny, nx])
print(cnt)
