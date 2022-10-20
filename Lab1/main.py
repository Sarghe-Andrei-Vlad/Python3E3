# 1. Find The greatest common divisor of multiple numbers read from the console.

num1 = int(input())
num2 = int(input())


def gdc(a, b):
    if (b == 0):
        return a
    else:
        return gdc(b, a % b)


print("GDC is: " + str(gdc(num1, num2)))


# 2. Write a script that calculates how many vowels are in a string.

def vowelCalculator(vowel, string):
    vowelCounter = 0
    for i in range(len(string)):
        if string[i] in vowel:
            vowelCounter += 1
    return vowelCounter


vowel = 'AEIOUaeiou'
string = "Ana has a lot of apples"

print("In the string " + str(string) + " there are " + str(vowelCalculator(vowel, string)) + " vowels")


# 3. Write a script that receives two strings and prints the number of occurrences of the first string in the second.

def occurrences(string1, string2):
    wordCounter = 0
    first_word = string1.split()
    second_word = string2.split()

    for i in range(len(first_word)):
        for j in range(len(second_word)):
            if first_word[i].lower() == second_word[j].lower():
                wordCounter += 1
    return wordCounter


string1 = 'mom'
string2 = 'Daniels mom is my mom'

print("Nr of occurences of the first string in the second one: " + str(occurrences(string1, string2)))


# 4. Write a script that converts a string of characters written in UpperCamelCase into lowercase_with_underscores.

def lowercase(text):
    for i in range(len(text)):
        if text[i].islower() == True and text[i + 1].isupper() == True:
            text = text[:i + 1] + "_" + text[i + 1:]
    text = text.lower()
    return text


print("The lower case form is: " + str(lowercase('UpperCamelCase')))


# 5. Given a square matrix of characters write a script that prints the string obtained by going through the matrix in spiral order (as in the example):
def spiral(matrix):

    rows = len(matrix)
    columns = len(matrix[0])
    top= 0
    left = 0
    while top < rows and left < columns:
        for i in range(left, columns):
            print(matrix[top][i], end="")
        top += 1

        for i in range(top, rows):
            print(matrix[i][rows - 1], end="")
        columns -= 1

        if top < rows:
            for i in range(columns - 1, left - 1, -1):
                print(matrix[rows - 1][i], end="")
            rows -= 1

        if left < columns:
            for i in range(rows - 1, top - 1, -1):
                print(matrix[i][left], end="")
            left += 1

matrix = [['f', 'i', 'r', 's'],
          ['n', '_', 'l', 't'],
          ['o', 'b', 'a', '_'],
          ['h', 't', 'y', 'p']]

spiral(matrix)

print('')


# 6. Write a function that validates if a number is a palindrome.

def palindrome(check_palindrome_text):
    if (str(check_palindrome_text) == str(check_palindrome_text)[::-1]):
        print("The number is a palindrome")
    else:
        print("The number is not a palindrome")


palindrome(123321)

# 7. Write a function that extract a number from a text (for example if the text is "An apple is 123 USD", this function will return 123,
# or if the text is "abc123abc" the function will extract 123). The function will extract only the first number that is found.

import re


def first_number(big_text):
    numbers_from_text = re.findall('[0-9]+', big_text)
    print(numbers_from_text[0])


first_number('Dadada dsadasd wed ef kmewf 10421 skdal 24')


# 8. Write a function that counts how many bits with value 1 a number has.
# For example for number 24, the binary format is 00011000, meaning 2 bits with value "1"

def binarycounter(longnumber):
    binary_form = bin(longnumber).count('1')
    # counter = 0
    # while bin > 0:
    #     if bin % 10 == 1:
    #         counter += 1
    #     bin = bin // 10

    return binary_form


print('the number of 1s is:' + str(binarycounter(152)))


# 9. Write a functions that determine the most common letter in a string. For example if the string is "an apple is
# not a tomato", then the most common character is "a" (4 times). Only letters (A-Z or a-z) are to be considered.
# Casing should not be considered "A" and "a" represent the same character.


def max_frequency_function(textlung):
    max_frequency = {}
    for i in textlung:
        if i in max_frequency:
            max_frequency[i] += 1
        else:
            max_frequency[i] = 1
    my_result = max(max_frequency, key=max_frequency.get)
    print('frequent character= ' + my_result)


max_frequency_function('Salutare ma numesc Andrei')

# 10. Write a function that counts how many words exists in a text. A text is considered to be form out of words that
# are separated by only ONE space. For example: "I have Python exam" has 4 words.


def word_counter_function(sentence):
    word_counter = 0
    newSentence = sentence.split()
    for i in newSentence:
        word_counter += 1
    return word_counter


print(word_counter_function('Salutare ma numesc Andrei si am scris o fraza lunga'))