class Solution {
    fun solution(new_id: String): String {
        var answer: String = ""
        answer = new_id.lowercase()
        answer = answer.replace(Regex("[^a-z0-9._-]"), "")
        answer = answer.replace(Regex("\\.{2,}"), ".")
        answer = answer.trim('.')
        if (answer.length == 0) {
            answer = "a"
        } else if (answer.length >= 16) {
            answer = answer.substring(0..14)
            answer = answer.replace(Regex("\\.$"), "")
        }
        while (answer.length <= 2) {
            answer += answer.last()
        }
        return answer
    }
}