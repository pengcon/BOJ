from collections import defaultdict
string=list(input())
dict=defaultdict(int)
for i in string:
    dict[i]+=1
count=0
ans=[]
jjaksu=[]
holsu=[]
for j in dict.keys():
    for i in range(dict[j]//2):
        jjaksu.append(j)
    if dict[j]%2!=0:
        count+=1
        holsu.append(j)

if count>1:
    print("I'm Sorry Hansoo")
else:
    jjaksu.sort()
    if len(string)%2!=0:
        ans=jjaksu+holsu+jjaksu[::-1]
    else:
        ans=jjaksu+jjaksu[::-1]
    for k in ans:
        print(k,end='')