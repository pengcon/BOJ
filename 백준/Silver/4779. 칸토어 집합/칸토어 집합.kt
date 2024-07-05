
import java.util.Scanner
import kotlin.math.*
fun divide(n:Int) : String{
    if (n <= 1 ){
        return "-"
    }
    val st = StringBuilder()
    val div = (n / 3)
    val left= divide(div)
    val middle = StringBuilder()
    repeat(div){
        middle.append(" ")
    }
    st.append(left)
    st.append(middle)
    st.append(left)
    return st.toString()

}
fun main(args: Array<String>) = with(System.`in`.bufferedReader()) {

    try {
        while(true) {
            val n = readLine().toInt()
            println(divide(3.toDouble().pow(n).toInt()))
        }
    } catch (e: Exception) {
        close()
        return@with
    }


}