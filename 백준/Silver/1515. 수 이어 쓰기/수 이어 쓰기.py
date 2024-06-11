
string = input()
num = 0
L =len(string)
idx = 0

while(True):
    num += 1
    for i in str(num):
        if string[idx]== i:
            idx +=1
            if idx >= L:
                print(num)
                exit()