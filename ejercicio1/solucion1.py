def isPalindrome(word):
    word = word.lower().replace(" ", "")
    return word == word[::-1]