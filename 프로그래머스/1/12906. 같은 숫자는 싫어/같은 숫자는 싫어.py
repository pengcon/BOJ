def solution(arr):
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    answer=[arr[0]]
    before=arr[0]
    for i in range(1,len(arr)):
        if before!=arr[i]:
            answer.append(arr[i])
            before=arr[i]
    return answer