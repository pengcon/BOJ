n=int(input())
nums = list(map(int,input().split()))
lst = list(map(int,input().split()))
giho = []

for i in range(lst[0]):
    giho.append('+')

for i in range(lst[1]):
    giho.append('-')


for i in range(lst[2]):
    giho.append('*')


for i in range(lst[3]):
    giho.append('/')

visited = []

max_ans = -2e9
min_ans = 2e9
def back(temp,cnt):
    global max_ans
    global min_ans
    if cnt == n-1:
        max_ans = max(temp, max_ans)
        min_ans = min(temp, min_ans)
        return 
    for i in range(n-1):
        if i not in visited:
            visited.append(i)
            if giho[i]== '-':
                back(temp-nums[cnt+1],cnt+1)
            elif giho[i] == '+':
                back(temp+nums[cnt+1],cnt+1)
            elif giho[i] == '*':
                back(temp*nums[cnt+1],cnt+1)
            elif giho[i] == '/':
                back(int(temp/nums[cnt+1]),cnt+1)
            visited.pop()
back(nums[0],0)
print(max_ans)
print(min_ans)