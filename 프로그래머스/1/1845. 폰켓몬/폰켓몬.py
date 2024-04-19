def solution(nums):
    length=len(nums)//2
    s=set()
    for i in nums:
        s.add(i)
    if len(s)>length:
        answer=length
    else:
        answer=len(s)
    return answer