import java.util.*

data class Balloon(val idx: Int, val move: Int)

fun main() = with(System.`in`.bufferedReader()) {
    val queue = ArrayDeque<Balloon>()
    val n = readLine().toInt()
    val arr = readLine().split(" ")
    arr.forEachIndexed { idx, it ->
        queue.add(Balloon(idx + 1, it.toInt()))
    }
    val answer = ArrayList<Int>()
    while (true) {
        val cur = queue.remove()
        answer.add(cur.idx)
        if (queue.isEmpty()) break

        if (cur.move > 0) {
            repeat(cur.move - 1) {
                queue.addLast(queue.remove())
            }
        } else if (cur.move < 0) {
            repeat((-cur.move)) {
                queue.addFirst(queue.removeLast())
            }
        }
    }
    answer.forEach { print("$it ") }
}