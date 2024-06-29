data class User(
    val name: String,
    val level: Int
)

fun main() {
    val (p, m) = readln().split(" ").map { it.toInt() }
    val rooms = ArrayList<ArrayList<User>>()
    val users = ArrayList<User>()
    repeat(p) {
        val (level, name) = readln().split(" ")
        val newUser = User(name, level.toInt())
        users.add(newUser)
    }


    for (user in users) {

        var makeRoom = true
        for (room in rooms) {
            if ((user.level <= room[0].level + 10) && (user.level >= room[0].level - 10)) {
                if (room.size < m) {
                    room.add(user)
                    makeRoom = false
                    break
                }
            }
        }

        if (makeRoom) {
            rooms.add(arrayListOf(user))
        }


    }
    //방 출력
    for (room in rooms) {
        room.sortWith(compareBy { it.name })
        if (room.size == m) {
            println("Started!")
        } else {
            println("Waiting!")
        }
        for (player in room) {
            println("${player.level} ${player.name}")
        }
    }
}