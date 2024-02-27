def isPalindrome(word):
    word = word.lower().replace(" ", "")
    return word == word[::-1]

if __name__ == "__main__":
    print(isPalindrome(input("Ingresa una palabra o frase: \n")))