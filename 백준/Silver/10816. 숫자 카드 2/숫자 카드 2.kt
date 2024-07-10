fun main() =with(System.`in`.bufferedReader()){
    val nMap = HashMap<Int, Int>()
    val n = readLine().toInt()
    val nList = readLine().split(" ").map { it.toInt() }
    for (num in nList) {
        nMap[num] = nMap.getOrDefault(num, 0) + 1
    }
    val answer = StringBuilder()
    val m = readLine().toInt()
    val mList = readLine().split(" ").map { it.toInt() }

    for (ans in mList) {
        answer.append("${nMap.getOrDefault(ans, 0)} ")
    }
    print(answer.toString())

}