import java.util.*

data class Job(val num: Int, val callTime: Int, val playTime: Int)

class Solution {
    fun solution(jobs: Array<IntArray>): Int {
        val comparator = compareBy<Job> { it.playTime }.thenBy { it.callTime }.thenBy { it.num }
        val pq = PriorityQueue(comparator)
        
        jobs.sortBy { it[0] }
        
        // 전체 job 개수, 현재 job 개수, 현재 시간, 현재 job이 있는지 여부, job이 끝나는 시간, 걸린시간(answer)
        val jobCount = jobs.size
        var curJobCount = 0
        var jobTime = 0
        var onJob = false
        var endTime = -1
        var answer = 0
        var hardDisk: Job? = null
        var endCount = 0
        // job이 다 돌기 전까지 
        while (true) {
            // 시간이 일치하면 우선순위 큐에 추가
            while (curJobCount < jobCount && jobs[curJobCount][0] <= jobTime) {
                pq.add(Job(num = curJobCount, callTime = jobs[curJobCount][0], playTime = jobs[curJobCount][1]))
                curJobCount += 1
            }
            // 하드에 job이 있을 때 끝나는 시간이라면
            if (onJob) {
                if (endTime==jobTime){
                    answer += (endTime - hardDisk!!.callTime)
                    hardDisk = null
                    endTime = -1
                    onJob = false 
                    endCount += 1
                    if (jobCount <= endCount) break
                }    
            }
            //하드에 job이 없을 때 우선순위 큐에 값이 있다면 값을 추가
            if (!onJob) {
                if(pq.isNotEmpty()){
                    hardDisk = pq.poll()
                    endTime = jobTime + hardDisk.playTime
                    onJob = true
                }
            }
            //시간 올림
            jobTime += 1
        }
        return (answer/jobCount).toInt()
    }
}