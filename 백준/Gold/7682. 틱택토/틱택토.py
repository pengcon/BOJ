
def check(a,word):
    if word == a[0] == a[1] == a[2]:
        return True
    if word == a[3] == a[4] == a[5]:
        return True
    if word == a[6] == a[7] == a[8]:
        return True
    #세로
    if word == a[0] == a[3] == a[6]:
        return True
    if word == a[1] == a[4] == a[7]:
        return True  
    if word == a[2] == a[5] == a[8]:
        return True
    #대각
    if word == a[0] == a[4] == a[8]:
        return True
    if word == a[2] == a[4] == a[6]:
        return True
    return False
while True:
    a = input()
    if a =="end":
        break
    circle_count = 0
    x_count = 0
    # O,X 개수 새기
    for word in a :
        if word == "O":
            circle_count +=1
        elif word =="X":
            x_count +=1
    #O,X 개수 유효성
    if circle_count > x_count or abs(circle_count-x_count) > 1:
        print("invalid")
        continue
    if circle_count>4 or x_count>5:
        print("invalid")
        continue      
    
    ans_O = False
    ans_X = False

    ans_O = check(a,'O')
    ans_X = check(a,'X')
    if ans_O == False and ans_X == False:
        if circle_count + x_count == 9:
            print("valid")
            continue
    elif ans_O == True and ans_X == False:
        if circle_count == x_count:
            print("valid")
            continue
    elif ans_O == False and ans_X == True:
        if x_count - circle_count == 1:
            print("valid")
            continue
    print("invalid")
    continue