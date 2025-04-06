import java.util.*

data class Printer(val idx: Int, val priority: Int)

fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val pq = PriorityQueue<Int>(reverseOrder())
    repeat(n) {
        val num = readLine().toInt()
        when (num) {
            0 -> {
                if (pq.isEmpty()) {
                    println(0)
                } else {
                    println(pq.remove())
                }
            }
            else -> {
                pq.offer(num)
            }
        }
    }
}