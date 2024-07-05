class Solution {
    fun solution(players: Array<String>, callings: Array<String>): Array<String> {
        var answer: Array<String> = arrayOf<String>()
        val tempPlayers = players.toMutableList()
        // 값,인덱스 map
        val playerMap = HashMap<String,Int>()
        
        //map에 값 넣기 
        var index = 0
        for (player in tempPlayers){
            playerMap[player] = index
            index += 1
        }
        
        for (name in callings) {
            val idx = playerMap[name]!!
            val swapName = tempPlayers[idx-1]
            tempPlayers[idx-1] = tempPlayers[idx].also{tempPlayers[idx] = tempPlayers[idx-1]}
            playerMap[name] = idx - 1
            playerMap[swapName] = idx 
        }

        answer = tempPlayers.toTypedArray()
        
        return answer
    }
}