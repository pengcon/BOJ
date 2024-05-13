from collections import deque
string=input()
idx=0
in_tag=0
q=deque()

def print_after_tag():
    global q
    for i in range(len(q)):
        print(q.popleft(),end='')
    print(">",end='')

def print_before_sapce():
    global q
    for i in range(len(q)):
        print(q.pop(),end='')
    print(" ",end='')

def print_before_tag():
    global q
    for i in range(len(q)):
        print(q.pop(),end='')
    print("<",end='')

while idx<=len(string):
    #마지막 인덱스일 때 
    if idx==len(string):
        print_before_sapce()
        break
    if string[idx]=='<':
        in_tag+=1
        print_before_tag()
    elif string[idx]=='>':
        in_tag-=1
        print_after_tag()
    elif string[idx]==' ':
        if in_tag>0:
            q.append(string[idx])
        else:
            print_before_sapce()
    else: q.append(string[idx])
    idx+=1