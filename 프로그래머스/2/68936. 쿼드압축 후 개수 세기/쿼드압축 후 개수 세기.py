
def find(arr):
    ans=[0,0]
    len_arr=len(arr)
    if len_arr==1:
        if arr[0][0]==0:
            return [1,0]
        else:
            return [0,1] 
    count_zero=0
    count_one=0

    for i in arr:
        count_zero+=i.count(0)
        count_one+=i.count(1)
    if count_one==0:
        return [1,0]
    elif count_zero==0:
        return [0,1]
    else:
        arr_lup = [row[:int(len_arr/2)] for row in arr[:int(len_arr/2)]] 
        temp_lup=find(arr_lup)
        ans[0]+=temp_lup[0]
        ans[1]+=temp_lup[1]
        arr_rup = [row[int(len_arr/2):len_arr] for row in arr[:int(len_arr/2)]] 
        temp_rup=find(arr_rup)
        ans[0]+=temp_rup[0]
        ans[1]+=temp_rup[1]
        arr_ldown = [row[:int(len_arr/2)] for row in arr[int(len_arr/2):len_arr]] 
        temp_ldown=find(arr_ldown)
        ans[0]+=temp_ldown[0]
        ans[1]+=temp_ldown[1]
        arr_rdown = [row[int(len_arr/2):len_arr] for row in arr[int(len_arr/2):len_arr]] 
        temp_rdown=find(arr_rdown)
        ans[0]+=temp_rdown[0]
        ans[1]+=temp_rdown[1]
    return ans
def solution(arr):
    answer=find(arr)
    return answer
arr=[[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
