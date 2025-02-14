# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_5_A&lang=ja
"""
全てのループを作成することは現実的ではないのでbit全探索を用いる
"""
N = 5
A = [1, 5, 7, 10, 21]
M = 4
B = [2, 4, 17, 8]

Answer = ["No"] * M

for i in range(M):
    # yesかnoかを判定する対象の数値
    b = B[i]
    # jはどの桁までのbitを立てるかを決める
    # 仮にN=5の場合、2**5=32なので、0~31までの32通りを全探索する
    # 00001
    # 00010
    # 00011
    # ...
    # 11101
    # 11110
    # 11111
    for j in range(2**N):
        sum = 0
        is_ok = False
        # 要素数でループして1つずつ桁をずらす
        for k in range(N):
            # jは固定で、kで1桁ずつずらしている
            # &1は2進数の最下位桁を取得する
            if ((j >> k) & 1) == 1:
                sum += A[k]
            if sum == b:
                is_ok = True
        if is_ok:
            Answer[i] = "Yes"
            break

print(Answer)
