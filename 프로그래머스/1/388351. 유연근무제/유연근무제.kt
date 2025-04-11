class Solution {
    fun solution(schedules: IntArray, timelogs: Array<IntArray>, startday: Int): Int {
        var answer: Int = 0
        val size = schedules.size
        for (i in 0 until size){
            var nowday = startday
            var flag = true
            for (j in 0..6) { 
            if (nowday>7) nowday = 1
            if (nowday == 6 || nowday == 7){
                nowday += 1
                continue
            }
            val start = schedules[i]
            val end =timelogs[i][j]
            if (((end / 100) - (start / 100)) * 60 + (end % 100) - (start % 100) > 10){
                flag = false
                break
            }
            nowday += 1
            }
            if (flag) answer += 1
        }
        return answer
    }
}