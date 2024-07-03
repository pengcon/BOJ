import java.util.Scanner
fun main(args: Array<String>) = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val m = readLine().toInt()
    val alphabets = StringBuilder()
    for (num in 0..<n){
        alphabets.append((65+num).toChar())
    }
    val downAlphabets = StringBuilder(readLine())
    var hidden = -1
    val arr = ArrayList<String>()
    for (i in 0..<m){
        val line = readLine()
        if (line[0] == '?')
            hidden = i
        arr.add(line)
    }

    //위에서 아래로
    for (x in 0..<hidden){
        for (idx in 0..<n-1){
            if (arr[x][idx] == '-'){
                alphabets[idx] = alphabets[idx+1].also{alphabets[idx+1] = alphabets[idx]}
            }
        }
    }
    //아래에서 위로
    for (x in m-1 downTo hidden+1){
        for (idx in 0..<n-1){
            if (arr[x][idx] == '-'){
                downAlphabets[idx] = downAlphabets[idx+1].also{downAlphabets[idx+1] = downAlphabets[idx]}
            }
        }
    }

    val answer = ArrayList<Char>()
    for (i in 0..n-2){
        if (alphabets[i] != downAlphabets[i]){
            answer.add('-')
            downAlphabets[i] = downAlphabets[i+1].also{downAlphabets[i+1] = downAlphabets[i]}
        } else answer.add('*')

    }
    if (alphabets.toString() == downAlphabets.toString()) {
        answer.forEach { print(it) }
    }
    else {
        repeat(n-1){
            print('x')
        }
    }

}