import java.io.*
fun main() = with(System.`in`.bufferedReader()){
    val (n,k) = readLine().split(" ").map{it.toInt()}
    val foreignList = mutableListOf<IntArray>()

    repeat(n){
        val foreign = readLine().split(" ").map{it.toInt()}
        foreignList.add(intArrayOf(foreign[0],foreign[1],foreign[2],foreign[3],0))

    }
    foreignList.sortWith (compareBy(
        {-it[1]},
        {-it[2]},
        {-it[3]}
    ) )

    var rank = 1
    var temp = 0
    foreignList[0][4] = rank
    for (i in (0..<foreignList.size-1)){
        if (foreignList[i][1] > foreignList[i+1][1]){
            rank += 1 + temp
            foreignList[i+1][4] = rank
            temp = 0
        }
        else if (foreignList[i][1] == foreignList[i+1][1]){
            if (foreignList[i][2] > foreignList[i+1][2]) {
                rank += 1 + temp
                foreignList[i+1][4] = rank
                temp = 0

            }
            else if (foreignList[i][2] == foreignList[i+1][2]){
                if (foreignList[i][3] > foreignList[i+1][3]){
                    rank += 1 + temp
                    foreignList[i+1][4] = rank
                    temp = 0
                }
                else if (foreignList[i][3] == foreignList[i+1][3]){
                    foreignList[i+1][4] = rank
                    temp += 1
                }
            }
        }
    }
    for (i in 0..<foreignList.size){
        if (foreignList[i][0] == k){
            println(foreignList[i][4])
        }
    }
//    for (item in foreignList){
//        for (i in item){
//            print(i)
//        }
//        println("")
//    }
}