# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_4_B&lang=ja
S = [1, 2, 2, 4, 5]


def binary_search(A, target):
    left = 0
    right = len(A)-1
    while left <= right:
        # //2なので、中央または中央より左のインデックスが返される
        mid = (left+right)//2
        if S[mid] == target:
            return mid
        # mid+1をするのは、midがtargetでない場合、midはもう一度調べる必要がないため
        if A[mid] < target:
            left = mid+1
        # mid-1をするのは、midがtargetでない場合、midはもう一度調べる必要がないため
        else:
            right = mid-1
    return -1


print(binary_search(S, 1))
