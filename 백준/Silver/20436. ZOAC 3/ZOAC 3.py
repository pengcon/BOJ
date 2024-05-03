left={}
right={}
left['q']=(0,0)
left['w']=(0,1)
left['e']=(0,2)
left['r']=(0,3)
left['t']=(0,4)
left['a']=(1,0)
left['s']=(1,1)
left['d']=(1,2)
left['f']=(1,3)
left['g']=(1,4)
left['z']=(2,0)
left['x']=(2,1)
left['c']=(2,2)
left['v']=(2,3)
right['b']=(2,0)
right['n']=(2,1)
right['m']=(2,2)
right['y']=(0,1)
right['u']=(0,2)
right['i']=(0,3)
right['o']=(0,4)
right['p']=(0,5)
right['h']=(1,1)
right['j']=(1,2)
right['k']=(1,3)
right['l']=(1,4)

L,R=map(str,input().split())
string=list(input())

def left_click(key):
    global L
    cur_x,cur_y=left[L]
    key_x,key_y=left[key]
    time=abs(cur_x-key_x)+abs(cur_y-key_y)+1
    L=key
    return time

def right_click(key):
    global R
    cur_x,cur_y=right[R]
    key_x,key_y=right[key]
    time=abs(cur_x-key_x)+abs(cur_y-key_y)+1
    R=key
    return time

time=0
for i in range(len(string)):
    if string[i] in left.keys():
        time+=left_click(string[i])
    else:
        time+=right_click(string[i])
print(time)