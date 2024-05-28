def solution(numbers, hand):
    left=[3,0]
    right=[3,2]
    numpad=[[3,1],[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
    result=""
    
    for i in numbers:
        if i==1 or i==4 or i==7:
            result=result+"L"
            left=numpad[i]
        elif i==3 or i==6 or i==9:
            result=result+"R"
            right=numpad[i]
        else:
            left_len=abs(left[0]-numpad[i][0])+abs(left[1]-numpad[i][1])
            right_len=abs(right[0]-numpad[i][0])+abs(right[1]-numpad[i][1])
            if left_len>right_len:
                result=result+"R"
                right=numpad[i]
            elif left_len<right_len:
                result=result+"L"
                left=numpad[i]
            else:
                if hand=="left":
                    result=result+"L"
                    left=numpad[i]
                elif hand=="right":
                    result=result+"R"
                    right=numpad[i]
                
    return result