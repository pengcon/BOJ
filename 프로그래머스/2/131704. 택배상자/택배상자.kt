class Solution {
    fun solution(order: IntArray): Int {
        var answer: Int = 0
        val count = order.size
        val container = ArrayList<Int>()
        var containerSize = count 
        val subCon = ArrayList<Int>()
        var subConSize = 0
        var orderIdx = 0
        for (box in 1..count){
            container.add(box)
        }
        container.forEach{ box ->
            if (box == order[orderIdx]){
                answer +=1
                orderIdx += 1
                while((subConSize>0) && (subCon[subConSize-1] == order[orderIdx]) && orderIdx<count){
                 
                    subCon.removeLast()
                    answer += 1
                    subConSize -= 1
                    orderIdx +=1
                }
            } else {
                subCon.add(box)
                subConSize += 1
            }
        }
    
        return answer
}
}