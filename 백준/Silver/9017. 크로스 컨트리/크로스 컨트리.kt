fun main() = with(System.`in`.bufferedReader()) {

    val t = readLine()!!.toInt()
    repeat(t){
        var minScore = 9999
        var answer = -1
        var five = 9999
        var lastIndex = -1
        val n = readLine()!!.toInt()
        val players = Array(201){ ArrayList<Int>() }
        val maps = mutableMapOf<Int, IntArray>()
        val counts = mutableMapOf<Int, Int>()
        val input = readLine()!!.split(" ").map { it.toInt() }
        for (i in 0..<n) {

            counts[input[i]] = counts.getOrDefault(input[i], 0) + 1
        }
        //스코어 넣어줌
        var score = 1
        for (i in 0..<n) {

            if (counts[input[i]] == 6){
                players[input[i]].add(score)
                score += 1
                if (lastIndex<input[i]){
                    lastIndex = input[i]
                }
            }
        }
            for (idx in 1..lastIndex){
            if (counts[idx] == 6){
                // 5번과 6번을 빼고 값을 더한것을 넣어주고, 동일 시 비교할려고 5번값도 넣어줌
            val tempArr = intArrayOf(players[idx].sum() -players[idx][4] - players[idx][5] , players[idx][4])
            maps[idx] = tempArr
            }
        }
        val keys =maps.keys
//        for (j in keys){
//            for (k in maps[j]!!){
//                print("$j = $k ")
//            }
//        }
        for (j in keys){
            if (minScore > (maps[j]?.get(0) ?: -1)){
                minScore = maps[j]?.get(0)!!
                answer = j
                five = maps[j]?.get(1)!!
            }
            else if (minScore == (maps[j]?.get(0) ?: -1)){
                if (five > maps[j]?.get(1)!!){
                    minScore = maps[j]?.get(0)!!
                    answer = j
                    five = maps[j]?.get(1)!!
                }

            }

        }
        println(answer)
    }


    }

