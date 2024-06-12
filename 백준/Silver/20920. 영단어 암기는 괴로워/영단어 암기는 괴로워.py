from collections import defaultdict
N, M = map(int, input().split())
dictionary = []
dict = defaultdict(int)
for _ in range(N):
    word = input()
    if len(word) >= M:
        dict[word] += 1
for i in dict.keys():
    dictionary.append([dict[i],len(i),i])
ans = sorted(dictionary, key=lambda x: (-x[0],-x[1],x[2]))
for i in ans:
    print(i[2])