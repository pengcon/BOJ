class Solution {
    fun solution(n: Int, w: Int, num: Int): Int {
      var answer = 0
    // 박스들을 담을 맵을 선언
    val boxes = HashMap<Int, ArrayList<Int>>()
    //count 초기화
    var count = 1
    // 번호 방향 플래그 선언
    var upFlag = true
    // 맵의 번호가 0~w-1까지 상승, 이후에는 w-1,0까지 하강을 반복
    // 반복하는 횟수는 count를 통하여 n이 될때까지 count 초기값 1
    for (boxCount in 0..w - 1) {
        boxes.put(boxCount, arrayListOf())
    }
    while (count <= n) {
        if (upFlag) {
            for (boxCount in 0..w - 1) {
                if (count > n) break
                boxes.getOrDefault(boxCount, arrayListOf<Int>()).add(count)
                count += 1
            }
            upFlag = false
        } else {
            for (boxCount in w - 1 downTo 0) {
                if (count > n) break
                boxes.getOrDefault(boxCount, arrayListOf<Int>()).add(count)
                count += 1
            }
            upFlag = true
        }
    }
    for (key in boxes.keys) {
        println(boxes.getOrDefault(key, arrayListOf<Int>()))
    }
    // 맵을 순회하며 해당 상자 번호가 있는지 확인
    for (key in boxes.keys) {
        if (num in boxes.getOrDefault(key, arrayListOf<Int>())) {
            val answerValue = boxes.getOrDefault(key, arrayListOf<Int>())
            for (value in answerValue) {
                if (value >= num) answer += 1
            }
            // 상자 번호가 일return answer
        }
    }
    return answer
    }
}