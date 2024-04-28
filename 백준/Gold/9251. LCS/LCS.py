first=list(input())
first=['']+first
first_length=len(first)
second=list(input())
second=['']+second
second_length=len(second)
LCS=[[0 for _ in range(second_length)] for _ in range(first_length)]
# print(LCS)
for i in range(1,first_length):
    for j in range(1,second_length):
        # print(i,j)
        if first[i] == second[j]:
            LCS[i][j]=LCS[i-1][j-1]+1
        elif first[i] != second[j]:
            LCS[i][j] = max(LCS[i-1][j],LCS[i][j-1])
print(LCS[first_length-1][second_length-1])