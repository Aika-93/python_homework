#Task_1: Hello!
def hello():
    return "Hello!"

result = hello()
print(result)


#Task_2: Greet with a Formatted String
def greet(name):
    return f"Hello, {name}!"

result = greet("Aiperi")
print(result)


#Task_3: Calculator
def calc(a, b, c = "multiply"):
    if c == "add":
        return a + b
    elif c == "subtract":
        return a - b
    elif c == "multiply":
        try:
            return a * b
        except:
            return f"You can't multiply those values!"
    elif c == "divide":
        try: 
            return a / b
        except ZeroDivisionError:
            return f"You can't divide by 0!"
        except:
            return f"You can't divide those values!"
    elif c == "modulo":
        return a % b
    elif c == "int_divide":
        return a // b
    return result

result = (calc("as", "as", "multiply"))
print(result)


#Task_4: Data Type Conversion
def data_type_conversion(value, type):
    if type == "float":
        try:
            return float(value)
        except:
            return f"You can't convert {value} into a {type}."
    elif type == "str":
        return str(value)
    elif type == "int":
        try:
            return int(value)
        except:
            return f"You can't convert {value} into a {type}."
    
result = data_type_conversion("banana", "int")
print(result)


#Task_5: Grading System, Using *args
def grade(*args):
    try:
        result = sum(args) / len(args)
        if result >= 90:
            return "A"
        elif 80 <= result <= 89:
            return "B"
        elif 70 <= result <= 79:
            return "C"
        elif 60 <= result <= 69:
            return "D"
        elif result <= 60:
            return "F"
    except:
        return f"Invalid data was provided."
    
result = grade("70", 80, 90)
print(result)


#Task_6: Use a For Loop with a Range
def repeat(string, count):
    for i in range(count):
        return string * count

result = repeat("Aika ", 5)
print(result)


#Task_7: Student Scores, Using **kwargs
def student_scores(x, **kwargs):
    if x == "best":
        for key, value in kwargs.items():
            if value == max(kwargs.values()):
                return key
    elif x == "mean":
        for key, value in kwargs.items():
            return sum(kwargs.values()) / len(kwargs.keys())



result = student_scores("mean", John = 23, Peri = 78, Ademi = 55, Alim = 20)
print(result)


#Task_8: Titleize, with String and List Operations
def titleize(text):
    words = text.split()
    little_words = ("a", "on", "an", "the", "of", "and", "is","in")
    for i, word in enumerate(words):
        if i == 0:
            words[i] = words[i].capitalize()
            continue
        if i == len(words) - 1:
            words[i] = words[i].capitalize()
            continue
        if word not in little_words:
            words[i] = word.capitalize()
        else:
            words[i] = word

    
    return " ".join(words)

result = titleize("war and peace")
print(result)


#Task_9: Hangman, with more String Operations
def hangman(secret, guess):
    result = ""
    for i, letter in enumerate(secret):
        if secret[i] in guess:
            result += letter
        else:
            result += "_"
    return result

result = hangman("Aiperi","ic")
print(result)


#Task_10: Pig Latin, Another String Manipulation Exercise
def pig_latin(sentence):
    words = sentence.split()
    result = []
    vowel = "aeiou"
    for word in words:
        if word[0] in vowel:
            result.append(word + "ay")
            continue
        if word[0] not in vowel and word[1:3] == "qu":
            result.append(word[3:] + word[0] + "qu" + "ay")
            continue
        if word[:2] == "qu":
            result.append(word[2:] + "qu" + "ay")
            continue
        if word[0] not in vowel and word[1] not in vowel:
            result.append(word[2:] + word[0] + word[1] + "ay")
            continue
        else:
            if word[0] not in vowel:
                result.append(word[1:] + word[0] + "ay")
    return " ".join(result)


result = pig_latin("apple")
print(result)