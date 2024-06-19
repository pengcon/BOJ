import java.io.*
fun main() {
    var answer = 0
    val br = BufferedReader(InputStreamReader(System.`in`))
    val input = br.readLine().split(" ").map { it.toInt() }
    val a = input[0]
    val b = input[1]
    val c = input[2]
    val list = List(101) { 0 }.toMutableList()
    for (i in 1..3) {
        val input2 = br.readLine().split(" ").map { it.toInt() }
        val start = input2[0]
        val end = input2[1]
        for (j in start..< end) {
            list[j] += 1
        }

    }
    for (i in 1..100){
        if (list[i] == 1) {
            answer += a
        }
        else if (list[i] == 2) {
            answer += b * list[i]
        }
        else if (list[i] == 3) {
            answer += c * list[i]
        }
    }
    print(answer)
}