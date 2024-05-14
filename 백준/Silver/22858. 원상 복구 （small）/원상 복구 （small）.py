import sys

input = sys.stdin.readline
N, K = map(int, input().split())
lists = [0] + list(map(int, input().split()))

D = [0] + list(map(int, input().split()))

new = [0 for i in range(N + 1)]

for i in range(K):
    for j in range(1, N+1):
        if i % 2 == 0:
            new[D[j]] = lists[j]
        else:
            lists[D[j]] = new[j]
if K % 2 == 0:
    for i in range(1, N+1):
        print(lists[i], end=' ')

else:
    for i in range(1, N+1):
        print(new[i], end=' ')
