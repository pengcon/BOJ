val maps = hashMapOf(
    "zer" to '0',
    "one" to '1',
    "two" to '2',
    "thr" to '3',
    "fou" to '4',
    "fiv" to '5',
    "six" to '6',
    "sev" to '7',
    "eig" to '8',
    "nin" to '9',
)
class Solution {
    fun solution(s: String): Int {
        var stringAnswer = ""
        var answer: Int= 0
        var idx = 0
        while (idx <= s.lastIndex) {
            if (s[idx].isDigit()){
                stringAnswer += s[idx]
                idx += 1
            }
            else {
                val sub = s.substring(idx..idx+2)
                stringAnswer += maps[sub]
                when(maps[sub]){
                    '0','4','5','9' -> idx += 4
                    '3','7','8' -> idx += 5
                    else -> idx += 3
                }
            }
        }
        print(stringAnswer)
        answer = stringAnswer.toInt()
        return answer
    }
}