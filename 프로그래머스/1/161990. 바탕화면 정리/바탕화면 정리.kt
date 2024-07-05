import kotlin.math.*
class Solution {
    fun solution(wallpaper: Array<String>): IntArray {
        var answer: IntArray = intArrayOf()
        val ySize = wallpaper[0].length
        // 순회
        var minX = 100
        var minY = 100
        var maxX = -1
        var maxY = -1
        for (i in wallpaper.indices) {
            for (j in 0 until ySize) {
                if (wallpaper[i][j] =='#'){
                    //minX 갱신
                    minX = min(minX,i)
                    //maxX 갱신
                    maxX = max(maxX,i+1)
                    //minY 갱신
                    minY = min(minY,j)
                    //maxY 갱신
                    maxY = max(maxY,j+1)
                }
            }
        }
        answer = intArrayOf(minX,minY,maxX,maxY)
        return answer
    }
}