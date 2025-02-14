# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_B&lang=ja
N = 6
G = [
    [2, 3],
    [3, 4],
    [5,],
    [6,],
    [6,],
    []
]

# 深さ優先探索
hakken = [0 for _ in range(len(G))]
syuryo = [0 for _ in range(len(G))]
# 訪問済みのノードを記録するリスト
visit = []


def dfs(pos, cnt):
    hakken[pos-1] = cnt
    visit.append(pos)
    for point in G[pos-1]:
        if point in visit:
            continue
        # 進むときにcntを増やす
        cnt += 1
        # いったん深さ優先で探索を行う
        cnt = dfs(point, cnt)
        # 深さ優先で進み終わったら、戻る
        # 戻るときにもcntを増やす
        cnt += 1
    syuryo[pos-1] = cnt+1  # 正直ここの+1は問題に合わせるためでよく分かっていない。
    return cnt


dfs(1, 1)
print(visit)
print(hakken)
print(syuryo)
