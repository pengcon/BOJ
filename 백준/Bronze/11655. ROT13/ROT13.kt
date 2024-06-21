import java.io.*
fun main() = with(System.`in`.bufferedReader()) {
    val input = readLine()
    for (s in input){
        if (s.isUpperCase()) {
            if (s.code > 77) {
                print(s - 13)
            }
            else {
                print(s + 13)
            }
        }
        else if (s.isLowerCase()){
            if (s.code >109){
                print(s-13)
            }
            else {
                print(s +13)
            }
        }
        else {
            print(s)
        }

    }
}