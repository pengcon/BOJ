fun main() {
    val (n, score, p) = readln().split(" ").map{it.toInt()}
    var input = listOf<Int>()
    if (n > 0){
        input = readln().split(" ").map{it.toInt()}
    }
    var temp = listOf<Int>()

    val scoreList = arrayListOf<Int>()
    for (i in input) {
        scoreList.add(i)
    }

    if (n == p){
        if (score > scoreList.last())
            scoreList[scoreList.lastIndex] = score
        else {
            print(-1)
            return
        }
    }
    else {
        scoreList.add(score)
    }
    scoreList.sort()
    scoreList.reverse()
    var rank = 0
    var equal = 0
    var beforeScore = 2_000_000_001
    for (i in 0..n){


        if (scoreList[i] < beforeScore){
            rank += 1 + equal
            beforeScore = scoreList[i]
            equal = 0
        } else {
            equal += 1
        }

        if (scoreList[i] == score) {
            print(rank)
            break
        }



    }

}