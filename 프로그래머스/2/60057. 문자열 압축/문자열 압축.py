def count_equal(s,idx,cut):
    count = 1
    string = s[idx : idx + cut]
    while(True):
        idx = idx+cut

        
        if string == s[idx : idx+cut]:
            count += 1
        else:
            return idx,count,string     
def make_small(s,cut):
    idx = 0
    small_s=""
    while(idx<len(s)):
        idx, count, string = count_equal(s,idx,cut)
        if count>1:
            small_s = small_s + str(count) + string
        else:
            small_s = small_s +  string
    return len(small_s)
        
    
def solution(s):
    answer = 0
    min_len = 1001
    for cut in range(1,len(s)+1):
        min_len = min(min_len , make_small(s,cut))
    answer = min_len
    return answer
