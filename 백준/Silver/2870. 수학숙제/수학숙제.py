N = int(input())
num = []
for _ in range(N):
    string = input()
    temp = ""
    for i in range(len(string)):
        if string[i].isdigit():
            temp = temp + string[i]
        else:
            if temp != "":
                num.append(int(temp))
                temp =""
    if temp != "":
        num.append(int(temp))
num.sort()
for i in num:
    print(i)