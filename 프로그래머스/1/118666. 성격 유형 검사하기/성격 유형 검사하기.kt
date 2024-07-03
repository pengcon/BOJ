class Solution {
    fun question(maps : HashMap<Char,Int>, category : String, score : Int){
        when(score){
            1 -> maps[category[0]] = maps.getOrDefault(category[0], 0) + 3
            2 -> maps[category[0]] = maps.getOrDefault(category[0], 0) + 2
            3 -> maps[category[0]] = maps.getOrDefault(category[0], 0) + 1
            5 -> maps[category[1]] = maps.getOrDefault(category[1], 0) + 1
            6 -> maps[category[1]] = maps.getOrDefault(category[1], 0) + 2
            7 -> maps[category[1]] = maps.getOrDefault(category[1], 0) + 3
        }
    }
    fun solution(survey: Array<String>, choices: IntArray): String {
        var answer: String = ""
        val maps = hashMapOf(
        'R' to 0,
        'T' to 0,
        'C' to 0,
        'F' to 0,
        'J' to 0,
        'M' to 0,
        'A' to 0,
        'N' to 0,
        )
        for (idx in survey.indices){
            question(maps,survey[idx],choices[idx])            
        }

        //1번 지표
        if (maps['R']!! >= maps['T']!!){
            answer += 'R'
        } else answer += 'T'
        //2번 지표
         if (maps['C']!! >= maps['F']!!){
            answer += 'C'
        } else answer += 'F'
        //3번 지표
         if (maps['J']!! >= maps['M']!!){
            answer += 'J'
        } else answer += 'M'
        //4번 지표
         if (maps['A']!! >= maps['N']!!){
            answer += 'A'
        } else answer += 'N'
        
        return answer
    }
}