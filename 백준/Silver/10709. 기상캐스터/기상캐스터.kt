import java.io.*
fun main() = with(System.`in`.bufferedReader()) {
    val (h,w) = readLine().split(" ").map{it.toInt()}
    val arr = Array(h) { IntArray(w) { -1 } }
    val cloud = Array(h) {Array<Char>(w) {'.'} }
    for (i in 0..<h){
        val input = readLine()
        for (j in 0..<w){
            cloud[i][j] = input[j]
        }
    }

    for (i in 0..<h){
        var day = -1
        for (j in 0..<w){
            if (cloud[i][j] == 'c'){
                day = 0
                arr[i][j] = day
            }
            else if (cloud[i][j] == '.'){
                if (day>=0){
                    day +=1
                    arr[i][j] = day
                }
            }
        }
    }

    for (i in arr){
        for (j in i){
            print("$j ")
        }
        println()
    }

}