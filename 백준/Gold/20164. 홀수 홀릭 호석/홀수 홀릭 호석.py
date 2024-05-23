# 14:13
from itertools import combinations

def count_holsu(number):
    holsu_count=0
    for i in number:
        if int(i)%2!=0:
            holsu_count+=1
    return holsu_count

def find_cases(len_num):
    nums = [ i for i in range(1,len_num)]
    nums_list=set(combinations(nums,2))
    return nums_list

def find_max_holsu(count,num):
    # print(len(num))
    ans=0
    len_num=len(num)
    if len_num==1:
        return count+count_holsu(num)
    elif len_num==2:
        count+=count_holsu(num[0])
        count+=count_holsu(num[1])
        new_num=str(int(num[0])+int(num[1]))
        #num에서 오류 뜨나 확인
        return find_max_holsu(count,new_num)
    elif len_num>2:
        for i in find_cases(len_num):
            temp=[]
            temp_count=0
            temp.append(num[0:i[0]])
            temp.append(num[i[0]:i[1]])
            temp.append(num[i[1]:])
            for j in temp:
                temp_count+=count_holsu(j)
            new_num=str(int(temp[0])+int(temp[1])+int(temp[2]))
            ans=max(ans,find_max_holsu(count+temp_count,new_num))
        return ans
    

def find_min_holsu(count,num):
    ans=1e9
    len_num=len(num)
    if len_num==1:
        return count+count_holsu(num)
    elif len_num==2:
        count+=count_holsu(num[0])
        count+=count_holsu(num[1])
        new_num=str(int(num[0])+int(num[1]))
        #num에서 오류 뜨나 확인
        return find_max_holsu(count,new_num)
    elif len_num>2:
        for i in find_cases(len_num):
            temp=[]
            temp_count=0
            temp.append(num[0:i[0]])
            temp.append(num[i[0]:i[1]])
            temp.append(num[i[1]:])
            for j in temp:
                temp_count+=count_holsu(j)
            new_num=str(int(temp[0])+int(temp[1])+int(temp[2]))
            ans=min(ans,find_min_holsu(count+temp_count,new_num))
        return ans

num=input()
if len(num)<=2:
    min_ans=max_ans=find_max_holsu(0,num)
else:
    max_ans=find_max_holsu(0,num)
    min_ans=find_min_holsu(0,num)
print(min_ans, max_ans)