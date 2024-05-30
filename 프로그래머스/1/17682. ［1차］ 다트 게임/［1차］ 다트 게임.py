def solution(dartResult):
    idx=0
    arr_idx=-1
    arr=[]
    while idx<len(dartResult)-1:
        arr.append(int(dartResult[idx]))
        idx+=1
        arr_idx+=1
        if dartResult[idx]=='0':
            arr[arr_idx]=10
            idx+=1
        if dartResult[idx]=='D':
            arr[arr_idx]=arr[arr_idx]**2
        elif dartResult[idx]=='T':
            arr[arr_idx]=arr[arr_idx]**3
        idx+=1
        if idx>len(dartResult)-1:
            break
        
        if dartResult[idx]=="*":
            if arr_idx>0:
                arr[arr_idx]=arr[arr_idx]*2
                arr[arr_idx-1]=arr[arr_idx-1]*2
                idx+=1
            else:
                arr[arr_idx]=arr[arr_idx]*2
                idx+=1 
        elif dartResult[idx]=="#":
            arr[arr_idx]= -arr[arr_idx]
            idx+=1 
    
    
    answer = sum(arr)
    return answer