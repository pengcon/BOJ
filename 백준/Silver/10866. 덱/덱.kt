fun main() = with(System.`in`.bufferedReader()) {
    val queue = ArrayDeque<Int>()
    val output = StringBuilder()
    val n = readLine().toInt()

    repeat(n) {
        val command = readLine().split(" ")
        when (command[0]) {
            "push_front" -> queue.addFirst(command[1].toInt())
            "push_back" -> queue.addLast(command[1].toInt())
            "pop_front" -> output.appendLine(queue.removeFirstOrNull() ?: -1)
            "pop_back" -> output.appendLine(queue.removeLastOrNull() ?: -1)
            "size" -> output.appendLine(queue.size)
            "empty" -> output.appendLine(if (queue.isEmpty()) 1 else 0)
            "front" -> output.appendLine(queue.firstOrNull() ?: -1)
            "back" -> output.appendLine(queue.lastOrNull() ?: -1)
        }
    }

    print(output)
}