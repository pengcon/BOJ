class Solution {
    fun solution(X: String, Y: String): String {
        var answer: String = ""
        var answerList = List<Int>(1){1}
        val xMap = hashMapOf('0' to 0,
                            '1' to 0,
                            '2' to 0,
                            '3' to 0,
                            '4' to 0,
                            '5' to 0,
                            '6' to 0,
                            '7' to 0,
                            '8' to 0,
                            '9' to 0)
        val yMap = hashMapOf('0' to 0,
                            '1' to 0,
                            '2' to 0,
                            '3' to 0,
                            '4' to 0,
                            '5' to 0,
                            '6' to 0,
                            '7' to 0,
                            '8' to 0,
                            '9' to 0)
    for (xc in X){

        xMap[xc] = xMap[xc]!! + 1 
    }     
    for (yc in Y){
        yMap[yc] = yMap[yc]!! + 1 
    } 
    var tempAns = ArrayList<Int>()
    for (key in xMap.keys){
        // print("${key}, ${xMap[key]}, ${yMap[key]} ")
        var count = 0
        if (xMap[key]!! > yMap[key]!!){
            count = yMap[key]!!
        } else count = xMap[key]!!

        for (i in 1..count){
            tempAns.add(key.toString().toInt())
        }
    }
    answerList = tempAns.sortedDescending()
    
    answer = answerList.joinToString("")
    if (answer == ""){
        answer = "-1"
    }
    else if (answer[0] == '0'){
        answer = "0"
    } 
    return answer
    }

}