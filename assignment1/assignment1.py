# test
#Task_1: Hello!
def hello():
    return "Hello!"

result = hello()


#Task_2: Greet with a Formatted String
def greet(name):
    return f"Hello, {name}!"

result = greet("Aiperi")


#Task_3: Calculator
operator = ("add", "subtract", "multiply", "divide", "modulo", "int_divide", "power")
def calc(a, b, operation = "multiply"):
    try:
        if operation == "add":
            return a + b
        elif operation == "subtract":
            return a - b
        elif operation == "multiply":
            return a * b
        elif operation == "divide":
            return a / b
        elif operation == "modulo":
            return a % b
        elif operation == "int_divide":
            return a // b
        elif operation == "power":
            return a ** b
        elif operation not in operator:
            return f"Wrong Operation"
            
    except ZeroDivisionError:
        return f"You can't divide by 0!"
    except TypeError:
        if operation == "add":
            return f"You can't add those values!"
        if operation == "subtract":
            return f"You can't subtract those values!"
        if operation == "multiply":
            return f"You can't multiply those values!"
        if operation == "divide":
            return f"You can't divide those values!"
        if operation == "modulo":
            return f"You can't modulo those values!"
        if operation == "int_divide":
            return f"You can't divide those values!"
        if operation == "power":
            return f"You can't power those values!"
    except Exception as e:
        return f"An error occured: {e}"
    

res = (calc(1,10, "add"))
print(res)


#Task_4: Data Type Conversion
target_type = ("int", "str", "float")
def data_type_conversion(value, datatype):
    try:
        if datatype == "float":
            return float(value)
        elif datatype == "str":
            return str(value)
        elif datatype == "int":
            return int(value)
        elif datatype not in target_type:
            return f"Wrong data type"
    except ValueError:
        return f"You can't convert {value} into a {datatype}."
    except Exception as e:
        return f"An error occured {e}"
    
result = data_type_conversion(20, "str")
print(result)


#Task_5: Grading System, Using *args
def grade(*args):
    try:
        average = sum(args) / len(args)
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        elif average <= 60:
            return "F"
    except ValueError:
        return f"Invalid data was provided."
    except TypeError:
        return f"Invalid data was provided."
    except Exception as e:
        return f"An error occured {e}"
    
result = grade(70, 60, 90)
print(result)


#Task_6: Use a For Loop with a Range
def repeat(string, count):
    for i in range(count):
        result = string * count
    return result

result = repeat("Aika ", 5)
print(result)


#Task_7: Student Scores, Using **kwargs
def student_scores(mode, **kwargs):
    try:
        if not kwargs:
            return f"Empty values"
        if mode == "best":
            max_value = max(kwargs.values())
            for key, value in kwargs.items():
                if value == max_value:
                    return key
        elif mode == "mean":
            return sum(kwargs.values()) / len(kwargs)
        else:
            return f"Wrong mode"
    except TypeError:
        return f"Type Error"
    except Exception as e:
        return f"An error occured {e}"
    

result = student_scores("best", John = 24, Aika = 78, Daniel = 56, Chase = 89)
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
        if word.lower() not in little_words:
            words[i] = word.capitalize()
        else:
            words[i] = word.lower()

    
    return " ".join(words)

result = titleize("war and The peace")
print(result)


#Task_9: Hangman, with more String Operations
def hangman(secret, guess):
    result = ""
    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"
    return result

result = hangman("Aiperi","pi")
print(result)


#Task_10: Pig Latin, Another String Manipulation Exercise
def pig_latin(sentence):
    words = sentence.split()
    result = []
    vowel = "aeiou"
    for word in words:
        if word[:2] == "qu":
            for i in range(2, len(word)):
                if word[i] in vowel:
                    break
            result.append(word[i:] + word[:2] + "ay")
            
        elif word[0] not in vowel:
                i = 0
                while i < len(word):
                    if word[i] in vowel:
                        break
                    if word[i] == "q" and i + 1 < len(word) and word[i + 1] == "u":
                        i += 2
                        break
                    i += 1
                result.append(word[i:] + word[:i] + "ay")
        else:
            result.append(word + "ay")
    return " ".join(result)


result = pig_latin("string")
print(result)