#Task 1: Hello
def hello():
    return "Hello!"


#Task 2: Greet with a Formatted String
def greet(name):
    return f"Hello, {name}!"


#Task 3: Calculator
def calc(value1, value2, operation="multiply"):
    try:
        if operation == "add":
            return value1 + value2
        elif operation == "subtract":
            return value1 - value2
        elif operation == "multiply":
            return value1 * value2
        elif operation == "divide":
            return value1 / value2
        elif operation == "modulo":
            return value1 % value2
        elif operation == "int_divide":
            return value1 // value2
        elif operation == "power":
            return value1 ** value2
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"
    

#Task 4: Data Type Conversion
def data_type_conversion(value, data_type):
    try:
        if data_type =="float":
            return float(value)
        elif data_type == "int":
            return int(value)
        elif data_type == "str":
            return str(value)
    except ValueError:
        return f"You can't convert {value} into a {data_type}."
    

#Task 5: Grading System, Using *args
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
        else:
            return "F"
    except TypeError:
        return f"Invalid data was provided."

#Task 6: Use a For Loop with a Range
def repeat(string, count):
    result = ""

    for i in range(count):
        result += string

    return result

#Task 7: Student Scores using **kwargs
def student_scores(option, **kwargs):
    
    if option == "best":
        highest_score = -1
        best_student = ""

        for student, score in kwargs.items():
            if score > highest_score:
                highest_score = score
                best_student = student
        return best_student
    
    elif option == "mean":
        return sum(kwargs.values()) / len(kwargs)

#Task 8: Titleize with String and List Operations
def titleize(title):
    words=title.split()
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    for i, word in enumerate(words):
        if i == 0:
            words[i]=word.capitalize()
        elif i == len(words)-1:
            words[i]=word.capitalize()
        elif word in little_words:
            pass
        else:
            words[i]=word.capitalize()

    return " ".join(words)
    
#Task 9: Hangman with more string operations
def hangman(secret, guess):
    answer = ""
    for letter in secret:
        if letter in guess:
            answer += letter
        else:
            answer += "_"

    return answer

#Task 10:  Pig Latin, Another String Manipulation Exercise
def pig_latin(phrase):
    vowels="aeiou"
    pig_latin_words = []

    for word in phrase.split():
                           
        if word[0] in vowels:
            pig_latin_words.append(word + "ay")

        else:
            index = 0

            while index < len(word):
                if word[index:index+2] == "qu":
                    index+=2
                elif word[index] not in vowels:
                    index += 1
                else:
                    break

            pig_latin_words.append(word[index:]+word[:index]+"ay")

    return " ".join(pig_latin_words)