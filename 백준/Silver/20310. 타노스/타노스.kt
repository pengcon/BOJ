fun main() {
    val st = readln()
    val arr = ArrayList<Char>()
    for (s in st){
        arr.add(s)

    }
    val zeroNum = st.count{it == '0'}
    val oneNum = st.count{it == '1'}
    val halfZeroNum = zeroNum / 2
    val halfOneNum = oneNum / 2

    for (i in 1..halfZeroNum){
        for (idx in arr.indices.reversed()){
            if ( (arr[idx]) == '0' ){
                arr.removeAt(idx)
                break
            }
        }
    }

    for (i in 1..halfOneNum){
        for (idx in arr.indices){
            if ( (arr[idx]) == '1' ){
                arr.removeAt(idx)
                break
            }
        }
    }
    for (a in arr){
        print(a)
    }
}