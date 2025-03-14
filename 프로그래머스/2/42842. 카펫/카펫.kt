import kotlin.math.sqrt
class Solution {
    fun solution(brown: Int, yellow: Int): IntArray {
        var garo = sqrt(yellow.toDouble()).toInt()
        val answer = IntArray(2){0}
        while (true){
            for (sero in 1..garo) {
                if ((sero*garo == yellow) && ((sero+2)*(garo+2) - yellow == brown)){
                    answer[0] = garo+2
                    answer[1] = sero+2
                }
            }
            if (answer[0] != 0){
                break
            } else{
                garo += 1
            }
        }
        return answer
    }
}