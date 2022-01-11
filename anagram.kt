// naive anagram checker
// assumes all input are in lower-case

fun main() {

    val inputOne = "nameless"
    val inputTwo = "salesmen"
    // val inputThree = "geeksforgeeks"
    // split words into a list of characters
    // iterate through list and increment counter

    val tokensInputOne: List<String> = inputOne.split("").filter { it.isNotBlank() }
    val tokensInputTwo: List<String> = inputTwo.split("")

    val frequencyMapForInputOne = tokensInputOne.countEach()
    val frequencyMapForInputTwo = tokensInputTwo.countEach()

    if (frequencyMapForInputOne.size === frequencyMapForInputTwo.size) {
        
    }
}

fun List<String>.countEach(): MutableMap<String, Int> {
    val frequencyMap = mutableMapOf<String, Int>()

    this.forEach { character ->
        val retrievedCharacterCount = frequencyMap.getOrDefault(character, 0)
        frequencyMap[character] = retrievedCharacterCount + 1
    }

    return frequencyMap
}