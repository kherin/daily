fun main() {

    val s: String = "abcac"
    val n: Int = 10

    println("Result is ${repeatedString(s, n)}")
}

fun repeatedString(s: String, n: Int): Int {
    val characters: List<String> = s.split("").filter { it.isNotBlank() }
    val baseStringSize: Int = characters.size

    val repeatFactor: Int = n - (n % baseStringSize)
    println("repeatFactor: $repeatFactor")

    return 1
}
