import java.io.*
fun main(){


    val br = BufferedReader(InputStreamReader(System.`in`))
    val p = br.readLine().toInt()
    repeat(p) {
        var ans = 0
        val input = br.readLine().split(" ").map { it.toInt() }
        val t = input[0]
        val arr1 =ArrayList<Int>()
        arr1.add(input[1])
        var max = input[1]
        for (i in 2..20) {
            if (max < input[i]){
                max = input[i]
                arr1.add(input[i])
            }
            else if (max>input[i]){
                for (idx in 0..< arr1.size){
                    if (arr1[idx] > input[i]){
                        ans += arr1.size - idx
                        arr1.add(idx,input[i])
                        break
                    }
                }
            }

        }
        println("$t $ans")
    }
}