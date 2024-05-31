from collections import defaultdict
string=list(input())
# 디폴트값으로 0을 갖는 defaultdict 선언
dict=defaultdict(int)
#문자별로 딕셔너리에 개수를 넣어 줌
for i in string:
    dict[i]+=1
#개수가 홀수인 문자의 개수 
holsu_count=0
#정답 리스트
ans=[]
#좌우 대칭을 진행할 문자의 리스트
pelindrom=[]
#개수가 홀수인 문자를 담은 리스트
holsu=[]
#딕셔너리에 담긴 문자들 for문
for j in dict.keys():
    #문자의 개수의 절반만큼 팰린드롬 리스트에 담음
    for i in range(dict[j]//2):
        pelindrom.append(j)
    #문자의 개수가 홀수인 문자는 중앙에 둘 문자 하나만 홀수 리스트에 담음
    if dict[j]%2!=0:
        holsu_count+=1
        holsu.append(j)
#홀수가 두개 이상 있으면 팰린드롬 불가
if holsu_count>1:
    print("I'm Sorry Hansoo")
else:
    #사전순 출력을 위한 정렬
    pelindrom.sort()
    #홀수 개수인 문자가 있을 때
    if len(string)%2!=0:
        #좌우대칭으로 출력하고 중앙에 홀수 리스트를 넣어줌
        ans=pelindrom+holsu+pelindrom[::-1]
    else:
        ans=pelindrom+pelindrom[::-1]
    for k in ans:
        print(k,end='')