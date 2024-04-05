import sys
input=sys.stdin.readline

while True:
    try:
        X=int(input())*10_000_000
        N=int(input())
        legos=[]
        for _ in range(N):
            legos.append(int(input()))
        legos.sort()

        start=0 
        end=N-1 

        # end 구하기 
        while(start<=end):
            mid=(start+end)//2 
            #부등호는 생각해보기
            if legos[mid]>=X:
                end=mid-1
            else:
                start=mid+1
        flag=True
        start=0
        while(start<end): 
            # print(start,end)
            if legos[start]+legos[end]==X: 
                print("yes "+str(legos[start])+" "+str(legos[end]))
                flag =False
                break 
            elif legos[start]+legos[end]>X: 
                end-=1 
            else:
                start+=1
        if flag:
                print("danger")
    except:
        break











