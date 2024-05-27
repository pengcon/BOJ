string=input()
len_string=len(string)
ans=[]
ans.append(string)
while(len(ans)<len_string):
    temp=[]
    string_len=len(ans[-1])
    for i in range(string_len):
        temp.append(ans[-1][0:i]+ans[-1][i+1:string_len])
    temp.sort()
    ans.append(temp[0])
while(len(ans)>0):
    print(ans.pop())