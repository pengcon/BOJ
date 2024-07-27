class Solution {
    fun solution(today: String, terms: Array<String>, privacies: Array<String>): IntArray {
        var answer = ArrayList<Int>()
        var tSum = 0
        val (ty, tm, td) = today.split(".").map{it.toInt()}
        tSum += ty*28*12
        tSum += (tm-1) * 28
        tSum += td
        val termsMap = HashMap<String, Int>()
        for (term in terms){
            val (category,month) = term.split(" ")
            termsMap[category] = month.toInt()
        }
        var pNumber = 1
        for (p in privacies){
            val (pDate, category) = p.split(" ")
            var (py,pm,pd) = pDate.split(".").map{it.toInt()}
            var pSum = 0
            pSum += py*28*12
            pSum += (pm-1) * 28
            pSum += (termsMap[category]!!) * 28
            pSum += pd
            if (tSum>=pSum) answer.add(pNumber)
            pNumber = pNumber + 1
        }
        return answer.toIntArray()
    }
}