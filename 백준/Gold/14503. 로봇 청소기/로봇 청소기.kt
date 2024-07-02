fun main() {
    //북 동 남 서 (상 우 하 좌)
    val dx = intArrayOf(-1, 0, 1, 0)
    val dy = intArrayOf(0, 1, 0, -1)
    //로봇청소기 후진
    val bx = intArrayOf(1,0,-1,0)
    val by = intArrayOf(0,-1,0,1)
    val (n, m) = readln().split(" ").map { it.toInt() }
    // 청소기 위치와 방향
    var (rx, ry, dir) = readln().split(" ").map { it.toInt() }
    //배열 생성
    val arr = ArrayList<MutableList<Int>>()
    repeat(n) {
        arr.add(readln().split(" ").map { it.toInt() }.toMutableList())
    }

//    for (i in arr){
//        for (j in i){
//            print(j)
//        }
//        println()
//    }


    var moving = true
    var answer =  0

    while (moving) {
        // 1. 현재칸이 청소x -> 현재칸 청소
        if (arr[rx][ry] == 0) {
            answer += 1
            arr[rx][ry] = -1
        }
        // 주변 4칸중 청소되지 않은 빈 칸
        var dirty = 0
        // 주변 4칸중 청소되지 않은 빈 칸 찾기
        for (i in dx.indices){
            val nx = rx + dx[i]
            val ny = ry + dy[i]
            if (arr[nx][ny] == 0) {
                dirty += 1
            }
        }
        //2. 주변 4칸중 청소되지않은 빈칸이 없는 경우
        if (dirty == 0){
            //후진가능한지 확인
            val backx = rx + bx[dir]
            val backy = ry + by[dir]
            if (arr[backx][backy] == 1){
                moving = false
            }
            else {
                rx = backx
                ry = backy
            }
        }
        else if (dirty > 0){
            //반시계 90도 회전
            if (dir == 0) dir = 3
            else dir -= 1
            //바라보는 방향 앞쪽칸이 청소되지 않은 빈칸이면 한 칸 전진
            val frontx = rx + dx[dir]
            val fronty = ry + dy[dir]
            if (arr[frontx][fronty] == 0){
                rx = frontx
                ry = fronty
            }
        }

    }
    println(answer)
}