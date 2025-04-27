import string

def is_palindrome(text: str) -> bool:
    text = text.lower()
    text = text.replace(" ", "")
    punctuation = string.punctuation
    text = "".join(ch for ch in text if ch not in punctuation)
    return text == text[::-1]

assert is_palindrome("madam") == True
assert is_palindrome("race car") == True
assert is_palindrome("A man, a plan, a canal: Panama") == True
assert is_palindrome("hello") == False
assert is_palindrome("") == True
assert is_palindrome("Лёша на полке клопа нашёл") == True