class Solution {
    fun solution(s: String): Int {
        var answer = 0
        var x = '-'
        var x_count = 0 
        var another_count = 0
        for (word in s){
            if (x_count==0){
                x = word
                x_count += 1
            } else if (x==word){
                x_count += 1
            } else if (x!=word){
                another_count += 1
            }
            
            if (x_count == another_count){
                answer +=1
                x_count = 0 
                another_count = 0
            }
        }
        if ((x_count>0) or (another_count>0)){
            answer +=1
        }
        
        return answer
    }
}