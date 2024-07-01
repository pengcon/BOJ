fun main() {
    val s = readln()
    val zeroNum = s.count{it == '0'}
    val oneNum = s.count{it == '1'}
    val halfZeroNum = zeroNum / 2
    val halfOneNum = oneNum / 2
    var new = ""
    for (i in 1..halfZeroNum){
        new += '0'
    }
    for (i in 1..halfOneNum){
        new += '1'
    }
    print(new)
}