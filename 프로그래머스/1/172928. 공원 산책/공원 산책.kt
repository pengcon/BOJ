class Solution {
    
    fun solution(park: Array<String>, routes: Array<String>): IntArray {
    
         
        val arr = ArrayList<ArrayList<Char>>()
        val parkX = park.size
        val parkY = park[0].length
        // N S W E 
        val dx = listOf(-1, 1, 0, 0)
        val dy = listOf(0, 0, -1, 1)
        val dMap = mutableMapOf<String,Int>("N" to 0,"S" to 1, "W" to 2, "E" to 3 )
        repeat(parkX){
            arr.add(ArrayList<Char>())
        }
        var startX = -1
        var startY = -1
        for (x in 0 until parkX){
             for (y in 0 until parkY){
                if (park[x][y] == 'S'){
                    startX = x
                    startY = y
                }
                 arr[x].add(park[x][y])  
            }
        }
        arr.forEach{
            it.forEach{print(it)}
            println("")
        }
        
        for (r in routes){
            val (d, m) = r.split(" ")
            val i = dMap[d]!!
            val nx = startX + (dx[i] * m.toInt())
            val ny = startY + (dy[i] * m.toInt())
            if ((nx >= 0) && (nx < parkX) && (ny >=0) && (ny < parkY)) {
                var move = true
                var tempX = startX
                var tempY = startY
                repeat(m.toInt()){
                    tempX = tempX + dx[i]
                    tempY = tempY + dy[i]
                    if (arr[tempX][tempY] == 'X'){
                        move = false
                    }
                }
                
                if (move){
                 
                startX = nx
                startY = ny
               
                }
            }
        }

        
       
        val answer = intArrayOf(startX,startY)
        
        
        return answer
    }
}
