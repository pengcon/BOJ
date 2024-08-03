import kotlin.math.*
class Solution {
    fun solution(fees: IntArray, records: Array<String>): IntArray {
        val answer = ArrayList<Int>()
        
        val inMap = HashMap<Int, Int>()
        val outMap = HashMap<Int, Int>()
        
        //입출차 기록 map에 넣기
        records.forEach{
         val (time,num,move) = it.split(" ")
         val (hour, min) = time.split(":")
         
        if (move == "IN"){ //출차
             inMap[num.toInt()] = inMap.getOrDefault(num.toInt(),0) + (hour.toInt()*60) + min.toInt()
         } else { //출차 
             outMap[num.toInt()] = outMap.getOrDefault(num.toInt(),0) + (hour.toInt()*60) + min.toInt()
        }
         
        }  
        
        //출차 안했을 때 예외
        for (key in inMap.keys){
            if (inMap[key]!! >= outMap.getOrDefault(key,0)){
                outMap[key] = outMap.getOrDefault(key,0) + (23*60) +59
            }
        }
        
        //출차에서 입차 빼기
        for (key in inMap.keys.toList().sorted()){
         val moneyHour = outMap[key]!! - inMap[key]!!

         if (fees[0] >= moneyHour){
             answer.add(fees[1])
         } else {
             
             var plusHour = ((moneyHour-fees[0]) / fees[2].toDouble()).toInt()
             if (((moneyHour-fees[0]) / fees[2].toDouble())  > plusHour ){
                 plusHour += 1
             }
             println(plusHour)
             answer.add(fees[1] + (plusHour*fees[3]))
         }
        }
                
        return answer.toIntArray()
    }
}