import sys
input=sys.stdin.readline
table=[list(map(int,input().split())) for _ in range(19)]
len_table=19

def print_ans(i,j):
    print(table[i][j])
    print(i+1,end=" ")
    print(j+1,end="")

def garo(num,x,y,count):
    #가로가 막혔을 때
    if y>=len_table:
        return count
    elif count>5:
        return count
    if table[x][y]==num:
        return garo(num,x,y+1,count+1)
    elif table[x][y]!=num:
        return count
    
def sero(num,x,y,count):
    #가로가 막혔을 때
    if x>=len_table:
        return count
    elif count>5:
        return count
    if table[x][y]==num:
        return sero(num,x+1,y,count+1)
    elif table[x][y]!=num:
        return count

def diagonal_down(num,x,y,count):
    if x>=len_table or y>=len_table:
        return count
    elif count>5:
        return count
    if table[x][y]==num:
        return diagonal_down(num,x+1,y+1,count+1)
    elif table[x][y]!=num:
        return count

def diagonal_up(num,x,y,count):
    if x<0 or y>=len_table:
        return count
    elif count>5:
        return count
    if table[x][y]==num:
        return diagonal_up(num,x-1,y+1,count+1)
    elif table[x][y]!=num:
        return count
    
def filter_count_not_six_for_garo(i,j):
    if j-1==-1 or table[i][j]!=table[i][j-1]:
        return True
    else:
        return False
def filter_count_five_for_garo(i,j):
    if garo(table[i][j],i,j+1,1)==5:
        return filter_count_not_six_for_garo(i,j)


def filter_count_not_six_for_sero(i,j):
    if i-1==-1 or table[i][j]!=table[i-1][j]:
        return True
    else:
        return False
def filter_count_five_for_sero(i,j):
    if sero(table[i][j],i+1,j,1)==5:
        return filter_count_not_six_for_sero(i,j)



def filter_count_not_six_for_diagonal_down(i,j):
    if i-1==-1 or j-1==-1 or table[i][j]!=table[i-1][j-1] :
        return True
    else:
        return False
    
def filter_count_five_for_diagonal_down(i,j):
    if diagonal_down(table[i][j],i+1,j+1,1)==5:
        return filter_count_not_six_for_diagonal_down(i,j)


def filter_count_not_six_for_diagonal_up(i,j):
    if i+1==len_table or j-1==-1 or table[i][j]!=table[i+1][j-1]:
        return True
    else:
        return False
    
def filter_count_five_for_diagonal_up(i,j):
    if diagonal_up(table[i][j],i-1,j+1,1)==5:
        return filter_count_not_six_for_diagonal_up(i,j)


find_ans=False
for i in range(len_table):
    for j in range(len_table):
        if table[i][j]!=0:
            if filter_count_five_for_garo(i,j):
                print_ans(i,j)
                find_ans = True
                break
            elif filter_count_five_for_sero(i,j):
                print_ans(i,j)
                find_ans = True
                break
            elif filter_count_five_for_diagonal_down(i,j):
                    print_ans(i,j)
                    find_ans = True
                    break
            elif filter_count_five_for_diagonal_up(i,j):
                    print_ans(i,j)
                    find_ans = True
                    break
    if find_ans:
        break
if find_ans==False:
    print(0)