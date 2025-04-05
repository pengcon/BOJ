fun main() = with(System.`in`.bufferedReader()) {
    val queue = ArrayDeque<Int>()
    val output = StringBuilder()
    val n = readLine().toInt()

    repeat(n) {
        val command = readLine().split(" ")
        when (command[0]) {
            "push" -> queue.add(command[1].toInt())
            "pop" -> output.appendLine(queue.removeLastOrNull() ?: -1)
            "top" -> output.appendLine(queue.lastOrNull() ?: -1)
            "size" -> output.appendLine(queue.size)
            "empty" -> output.appendLine(if (queue.isEmpty()) 1 else 0)
        }
    }

    print(output)
}