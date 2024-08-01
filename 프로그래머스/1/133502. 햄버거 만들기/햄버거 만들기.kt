class Solution {
    fun solution(ingredient: IntArray): Int {
        var answer: Int = 0
        
        val newArray = ArrayList<Int>()
        var newSize = 0
        ingredient.forEach{
            newArray.add(it)
            newSize += 1
            if (newSize>=4){
                if ((newArray[newSize-1] == 1) && (newArray[newSize-2] == 3) && (newArray[newSize-3] == 2) && (newArray[newSize-4] == 1) ){
                    answer += 1
                    repeat(4){
                        newArray.removeLast()
                    }
                    newSize -= 4
                    
                }
            }
        }
    
        return answer
    }
}