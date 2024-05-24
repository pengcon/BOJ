N=int(input())
arr=[list(map(int,input().split())) for _ in range(N)]


def find(arr):
    len_arr=len(arr)
    half_arr=int(len(arr)/2)
    default=arr[0][0]
    ans=[0,0]
    equal=True
    for i in range(len_arr):
        for j in range(len_arr):
            if default!=arr[i][j]: equal=False
    if equal==True:
        ans[default]+=1
        return ans
    
    arr_lu=[i[:half_arr] for i in arr[:half_arr]]
    temp1,temp2=find(arr_lu)
    ans[0]+=temp1
    ans[1]+=temp2

    arr_ru=[i[half_arr:] for i in arr[:half_arr]]
    temp1,temp2=find(arr_ru)
    ans[0]+=temp1
    ans[1]+=temp2

    arr_ld=[i[:half_arr] for i in arr[half_arr:]]
    temp1,temp2=find(arr_ld)
    ans[0]+=temp1
    ans[1]+=temp2

    arr_rd=[i[half_arr:] for i in arr[half_arr:]]
    temp1,temp2=find(arr_rd)
    ans[0]+=temp1
    ans[1]+=temp2
    return ans
ans=find(arr)
print(ans[0])
print(ans[1])
