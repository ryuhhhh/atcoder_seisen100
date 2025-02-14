# https://atcoder.jp/contests/abc106/tasks/abc106_b
N = 105
result = []
for i in range(1, N+1):
    # 奇数だけを対象
    if i % 2 == 0:
        continue
    count = 0
    # 平方根とするのは、約数の個数を求める際に、十分だから
    # 例えば、12の約数は、1, 2, 3, 4, 6, 12で、6個だが
    # 12の平方根は、3.46...なので、3までで十分
    # 1*12, 2*6, 3*4の3つの組み合わせがある
    for j in range(1, int(i**0.5)):
        if i == j:
            count += 1
        elif i % j == 0:
            count += 2
    if count == 8:
        result.append(i)

print(len(result), result)
