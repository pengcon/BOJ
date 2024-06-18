from collections import defaultdict
from itertools import combinations
def solution(clothes):
    answer = 1
    wear = defaultdict(int)
    for i in clothes:
        wear[i[1]] += 1
    w = list(wear.keys())
    
    for i in w:
        answer = answer * (wear[i]+1) 
    
    
    answer -= 1
    return answer