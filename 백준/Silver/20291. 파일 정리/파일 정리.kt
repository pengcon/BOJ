fun main() {
    val n = readln().toInt()
    val files = HashMap<String, Int>()
    repeat(n) {
        val (name, extension) = readln().split(".")
        files[extension] = files.getOrDefault(extension, 0) + 1
    }
    val keys = (files.keys).sorted()

    for (key in keys) {
        println("$key ${files[key]}")
    }
}