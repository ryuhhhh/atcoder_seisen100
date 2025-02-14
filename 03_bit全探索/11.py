# https://atcoder.jp/contests/abc128/tasks/abc128_c

# Nは最大でも10なので2^10=1024のループが最大

N = 5
M = 2
# 各電球がつながっているスイッチのリスト
A = [[1, 2, 5], [2, 3]]
# 各電球のつながっているスイッチをONにした数を2で割った余り
P = [1, 0]

count = 0
# N個のスイッチのON/OFFの組み合わせを2進数で全探索
# iは0~2^N-1まで
for i in range(1 << N):
    # 5桁の2進数を文字列で作成
    # 例えばi=1の場合、00001となり、i=2の場合、00010となる
    s = bin(i)[2:].zfill(N)
    is_ok = True
    # 各電球でループ
    # ON/OFFの組み合わせを固定し、各電球の条件を満たすか確認
    for j in range(len(A)):
        a = A[j]
        sum = 0
        # 各電球の条件に記載されている各桁和を求める
        for pos in a:
            # 先ほど作成した2進数文字列から、各スイッチのON/OFFを取得
            sum += int(s[pos-1])
        if sum % 2 != P[j]:
            is_ok = False
    if is_ok:
        count += 1
print(count)
