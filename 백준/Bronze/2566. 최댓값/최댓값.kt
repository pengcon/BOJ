fun main() {
    val arr = Array(9) { IntArray(9) }
    for (i in arr.indices) {
        val input = readln().split(" ").map { it.toInt() }
        for (j in input.indices) {
            arr[i][j] = input[j]
        }
    }
    var maxX = -1
    var maxY = -1
    var maxNum = -1
    for (i in arr.indices) {
        for (j in arr[i].indices) {
            if (arr[i][j] > maxNum) {
                maxX = i
                maxY = j
                maxNum = arr[i][j]
            }
        }
    }
    println(maxNum)
    print("${maxX + 1} ${maxY + 1}")
}
