import java.util.Scanner

fun main(args: Array<String>) {
    val sc = Scanner(System.`in`)

    while (sc.hasNext()) {
        val N = sc.nextInt()
        var result = "-"

        repeat(N) {
            result = cantor(result)
        }

        println(result)
    }
}

private fun cantor(str: String): String {
    return str + " ".repeat(str.length) + str
}