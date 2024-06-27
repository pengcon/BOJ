import java.util.Scanner

fun main(args: Array<String>) {
    val n = readln().toInt()
    var goal1 = 0
    var goal2 = 0
    var winTime1 = 0
    var winTime2 = 0
    val timeLine = IntArray(2880)
    repeat(n) {
        val (team, time) = readln().split(" ")

        val (hour, minute) = time.split(":").map { it.toInt() }
        val goalTime = (hour * 60) + minute
        timeLine[goalTime] = team.toInt()
    }

    for (t in timeLine.indices) {
        when (timeLine[t]) {
            1 -> goal1 += 1
            2 -> goal2 += 1
        }
        if (goal1 > goal2) {
            winTime1 += 1
        } else if (goal1 < goal2) {
            winTime2 += 1
        }
    }

    var winHour1 = (winTime1 / 60).toString()
    if (winHour1.length == 1) winHour1 = "0$winHour1"
    var winHour2 = (winTime2 / 60).toString()
    if (winHour2.length == 1) winHour2 = "0$winHour2"
    var winMinute1 = (winTime1 % 60).toString()
    if (winMinute1.length == 1) winMinute1 = "0$winMinute1"
    var winMinute2 = (winTime2 % 60).toString()
    if (winMinute2.length == 1) winMinute2 = "0$winMinute2"

    println("$winHour1:$winMinute1")
    println("$winHour2:$winMinute2")
}