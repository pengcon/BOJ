class Solution {
    fun solution(lottos: IntArray, win_nums: IntArray): IntArray {
        val ranking = mapOf(6 to 1, 5 to 2 , 4 to 3, 3 to 4, 2 to 5, 1 to 6, 0 to 6)
        var answer: IntArray = intArrayOf()
        var zeroCount = 0
        var lottoCount = 0
        for (lotto in lottos){
            if (win_nums.contains(lotto)) lottoCount += 1
            else if (lotto==0) zeroCount += 1
        }
        answer = intArrayOf(ranking[lottoCount+zeroCount]!!,ranking[lottoCount]!!)

        return answer
    }
}