fun main() {
    val n = readln().toInt()
    val input = readln().split(" ").map { it.toInt() }
    val nums = ArrayList<Int>()
    for (i in n downTo 1) {
        nums.add(input[i - 1], i)
    }
    for (num in nums) {
        print("$num ")
    }

}