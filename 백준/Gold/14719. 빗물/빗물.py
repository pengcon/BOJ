from collections import defaultdict
H,W = map(int,input().split())
block_list = list(map(int,input().split()))
block_dict = defaultdict(int)
block_index=[[] for i in range(H+1)]
#그림 그리기
for i in range(W):
    temp=block_list[i]
    while temp>0:
        block_dict[temp]+=1
        block_index[temp].append(i)
        temp-=1
ans=0
for j in range(1,H+1):
    #같은 개수의 블록이 2개 이상 있을때 실행
    if block_dict[j]<2:
        continue
    else:
        # j 개수에 대해 첫 인덱스,마지막 인덱스를 구함
        first,last=min(block_index[j]),max(block_index[j])
        # first 부터 last 전 까지
        for k in range(first,last):
            #특정 인덱스의 값이 j보다 더 적다면 빗물 하나 추가.
            if block_list[k]<j:
                ans+=1
print(ans)

