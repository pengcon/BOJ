s = input()
num = ''
ans = 0
is_minus=False
for i in s:
    if i != '-' and i!= '+':
        num = num + i
    elif i == '+':
        if is_minus:
            ans -=int(num)
        else:
            ans+=int(num)
        num=''  
    elif i =='-':
        if is_minus:
            ans-= int(num)
        else:
            ans +=int(num)
            is_minus =True
        num=''    
if is_minus:
    ans-= int(num)
else:
    ans+= int(num)
print(ans)