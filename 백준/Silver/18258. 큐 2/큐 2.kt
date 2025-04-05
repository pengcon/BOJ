import java.util.*

fun main() = with(System.`in`.bufferedReader()) {
    val queue = LinkedList<Int>()
    val output = StringBuilder()
    val n = readLine().toInt()

    repeat(n) {
        val command = readLine().split(" ")
        when (command[0]) {
            "push" -> {
                queue.add(command[1].toInt())
            }

            "pop" -> {
                output.appendLine(queue.poll() ?: -1)
            }

            "front" -> {
                output.appendLine(queue.firstOrNull() ?: -1)
            }

            "empty" -> {
                output.appendLine(if (queue.isEmpty()) 1 else 0)
            }

            "back" -> {
                output.appendLine(queue.lastOrNull() ?: -1)
            }

            "size" -> {
                output.appendLine(queue.size)
            }
        }
    }

    print(output)
}
