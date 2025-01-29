import heapq
def solution(operations):
    max_heap=[]
    min_heap=[]
    count= 0
    for i in operations:
        op,num = i.split(" ")
        if op=="I":
            heapq.heappush(max_heap, (-int(num),int(num)))
            heapq.heappush(min_heap, int(num))
            count+=1
        elif op=="D":

            if num=="1" and count>0:
                del_num = heapq.heappop(max_heap)[1]
                min_heap.remove(del_num)
                count-=1
            elif num =="-1" and count > 0:
                del_num = heapq.heappop(min_heap)
                max_heap.remove((-del_num,del_num))
                count-=1
    answer = []
    if count>0:
        answer.append(heapq.heappop(max_heap)[1])
        answer.append(heapq.heappop(min_heap))
    else:
        answer= [0,0]
    return answer