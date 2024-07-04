import java.util.Scanner
fun main(args: Array<String>) = with(System.`in`.bufferedReader()) {
	val dList = readLine().split(" ")
	var ans = 0
	for (d in dList){
		if (d != ""){
			ans += 1
		}
	}
	print(ans)
}