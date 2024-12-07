a = input()

count = 0 
for i in range(97,123):
    for j in a:
        if j == chr(i):
            count+=1
    print(count,end=" ")
    count= 0 
