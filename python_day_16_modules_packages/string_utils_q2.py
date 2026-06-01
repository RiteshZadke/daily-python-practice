def conunt_vowels(text):
    vowels = 0
    for ch in text:
        if ch in 'AEIOUaeiou':
            vowels += 1
    
    return vowels

def reverse_string(text):
    return text[::-1]

def is_panlindrome(text):
    return text.lower() == text[::-1].lower