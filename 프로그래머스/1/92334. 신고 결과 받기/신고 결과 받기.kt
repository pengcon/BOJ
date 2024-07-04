class Solution {
    fun solution(id_list: Array<String>, report: Array<String>, k: Int): IntArray {
        var answer = intArrayOf()
        val tempAns = ArrayList<Int>()
        val reportMap = HashMap<String, ArrayList<String>>()
        val reportedMap = HashMap<String, Int>()
        for (id in id_list){
            reportMap[id] = ArrayList<String>()
            reportedMap[id] = 0
        }
        
        for (i in report.indices){
            val (reporter,reporteder) = report[i].split(" ")
            if(!(reporteder in reportMap[reporter]!!)) {
            reportedMap[reporteder] = reportedMap[reporteder]!! + 1 //주의
            reportMap[reporter]!!.add(reporteder)
            }
        }
        
        for (id in id_list){
            var score = 0
            for (r in reportMap[id]!!){
                
                if (reportedMap[r]!! >= k){
                    score += 1
                }
            }
            tempAns.add(score)
        }
        answer = tempAns.toIntArray()
        return answer
    }
}