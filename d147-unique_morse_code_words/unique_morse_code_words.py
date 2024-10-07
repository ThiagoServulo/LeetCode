def uniqueMorseRepresentations(words):
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    res = set()
    for word in words:
        aux  = ""
        for letter in word:
            index = letters.index(letter)
            aux += morse[index]
        res.add(aux)
    return len(res)

print(uniqueMorseRepresentations(["gin","zen","gig","msg"])) # 2