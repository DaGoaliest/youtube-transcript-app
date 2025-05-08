def censor_vowels(text):
    vowels = "aeiou"
    for char in vowels:
        text = text.replace(char, " ")
    return text 

print(censor_vowels("hello world")) # h ll  w rld
