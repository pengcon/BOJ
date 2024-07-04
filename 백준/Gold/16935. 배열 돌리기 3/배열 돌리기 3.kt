import java.util.Scanner
fun calculateOne(n : Int, m : Int, arr : ArrayList<MutableList<Int>>) : ArrayList<MutableList<Int>> {
    val tempArr = ArrayList<MutableList<Int>>()
    repeat(n){
        tempArr.add(MutableList(m){0})
    }
    for(c in 0 until m){
        for (r in 0 until n){
            tempArr[r][c] = arr[n-r-1][c]
        }
    }
    return tempArr
}

fun calculateTwo(n : Int, m : Int, arr : ArrayList<MutableList<Int>>) : ArrayList<MutableList<Int>> {
    val tempArr = ArrayList<MutableList<Int>>()
    repeat(n){
        tempArr.add(MutableList(m){0})
    }
    for(r in 0 until n){
        for (c in 0 until m){
            tempArr[r][c] = arr[r][m-c-1]
        }
    }
    return tempArr
}
fun calculateThree(n: Int , m : Int, arr : ArrayList<MutableList<Int>>) : ArrayList<MutableList<Int>> {
    val tempArr = ArrayList<MutableList<Int>>()
    repeat(m){
        tempArr.add(MutableList(n){0})
    }
    for (i in 0 until n){
        for (j in 0 until m){
            tempArr[j][n-i-1] = arr[i][j]
        }
    }
    return tempArr
}

fun calculateFour(n: Int , m : Int, arr : ArrayList<MutableList<Int>>) : ArrayList<MutableList<Int>> {
    val tempArr = ArrayList<MutableList<Int>>()
    repeat(m){
        tempArr.add(MutableList(n){0})
    }
    for (i in 0 until n){
        for (j in 0 until m){
            tempArr[m-j-1][i] = arr[i][j]
        }
    }
    return tempArr
}



fun calculateFive(n: Int , m : Int, arr : ArrayList<MutableList<Int>>) : ArrayList<MutableList<Int>> {
    val tempArr = ArrayList<MutableList<Int>>()
    repeat(n){
        tempArr.add(MutableList(m){0})
    }
    val x = n/2
    val y = m/2
    for (r in 0 until n/2){
        for (c in 0 until m/2){
            tempArr[r][c] = arr[r+x][c]
            tempArr[r][c+y] = arr[r][c]
            tempArr[r+x][c+y] = arr[r][c+y]
            tempArr[r+x][c] = arr[r+x][c+y]
        }
    }
    return tempArr
}

fun calculateSix(n: Int , m : Int, arr : ArrayList<MutableList<Int>>) : ArrayList<MutableList<Int>> {
    val tempArr = ArrayList<MutableList<Int>>()
    repeat(n){
        tempArr.add(MutableList(m){0})
    }
    val x = n/2
    val y = m/2
    for (r in 0 until n/2){
        for (c in 0 until m/2){
            tempArr[r][c] = arr[r][c+y]
            tempArr[r][c+y] = arr[r+x][c+y]
            tempArr[r+x][c+y] = arr[r+x][c]
            tempArr[r+x][c] = arr[r][c]
        }
    }
    return tempArr
}


fun main(args: Array<String>) = with(System.`in`.bufferedReader()){
    val (n, m, r) = readLine().split(" ").map{it.toInt()}
    var arr = ArrayList<MutableList<Int>>()
    val xHalf = n/2
    val yHalf = m/2
    val xSize = n - 1
    val ySize = m -1
    repeat(n){
        val line = readLine().split(" ").map{it.toInt()}.toMutableList()
        arr.add(line)
    }
    val calList = readLine().split(" ").map{it.toInt()}

    for (cal in calList){
        when (cal){
            1 -> arr = calculateOne(arr.size,arr[0].size,arr)
            2 -> arr = calculateTwo(arr.size,arr[0].size,arr)
            3 -> arr = calculateThree(arr.size,arr[0].size,arr)
            4 -> arr = calculateFour(arr.size,arr[0].size,arr)
            5 -> arr = calculateFive(arr.size,arr[0].size,arr)
            6 -> arr = calculateSix(arr.size,arr[0].size,arr)
        }
    }
    for (a in arr){
        for (j in a){
            print("$j ")
        }
        println()
    }
}