# https://atcoder.jp/contests/abc122/tasks/abc122_b
S = "ATCODER"

max_length = 0
for i in range(len(S)):
    length = 0
    for s in S[i:]:
        if s not in "ACGT":
            break
        length += 1
    max_length = max(max_length, length)

print(max_length)
