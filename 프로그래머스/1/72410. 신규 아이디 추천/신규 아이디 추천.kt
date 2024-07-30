class Solution {
    fun solution(new_id: String): String {
        var answer: String = ""
        answer = new_id.lowercase()
        answer = answer.replace(Regex("[^a-z0-9-_.]"),"")
        answer = answer.replace(Regex("\\.{2,}"),".")
        answer = answer.replace(Regex("^\\.|\\.$"),"")
        if (answer.length==0) answer = "a"
        if (answer.length>=16) {
            answer = answer.substring(0,15)
        answer = answer.replace(Regex("\\.$"),"")}
        if (answer.length<=2) {
            while(answer.length<3){
                answer = answer + answer[answer.length-1]
            }
        }
        print(answer)
        return answer
    }
}