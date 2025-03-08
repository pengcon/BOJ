class Solution {
    fun solution(players: IntArray, m: Int, k: Int): Int {
        val serverTimer = HashMap<Int,Int>()
        var serverCount = 0
        var addCount = 0
        
        (0..23).forEach{ time->
            serverCount -= serverTimer.getOrDefault(time,0)
            val neededServer = (players[time]/m).toInt()
            if (neededServer > serverCount) {
                val addedServer = neededServer-serverCount
                serverCount += addedServer
                addCount += addedServer
                serverTimer[time+k] = addedServer
            }
        }
        
        return addCount
    }
}