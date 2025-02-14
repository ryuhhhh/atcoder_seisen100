# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_7_B&lang=ja
a = []
n = 5
x = 9
count = 0
for i in range(1,n+1):
    for j in range(i+1,n+1):
        for k in range(j+1,n+1):
            if i+j+k == x:
                count += 1
print(count)