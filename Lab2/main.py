# 1. Write a function to return a list of the first n numbers in the Fibonacci string.
from itertools import count

from skimage.io import collection


def fibonacci(n):
    fib1 = 0
    fib2 = 1
    res = []
    for i in range(0, n):
        res.append(fib1)
        step = fib1 + fib2
        fib2 = fib1
        fib1 = step
    return res


print(fibonacci(7))

# 2. Write a function that receives a list of numbers and returns a list of the prime numbers found in it.

import math


def isPrime(number):
    if number == 0:
        return 0
    if number == 1:
        return 1
    if number % 2 == 0:
        return 0
    for i in range(3, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return 0
    else:
        return 1


def primeList(list):
    res = []
    for i in list:
        if isPrime(i):
            res.append(i)
    else:
        return res


print(primeList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]))


# 3. Write a function that receives as parameters two lists a and b and returns: (a intersected with b, a reunited with b, a - b, b - a)

def listOperations(a, b):
    print("union: ", set(a + b))
    print("intersection: ", set([value for value in a if value in b]))
    print("a - b:", set([value for value in a if value not in b]))
    print("b - a:", set([value for value in b if value not in a]))


listOperations([1, 2, 3, 4, 5], [0, 2, 4, 6, 8])


# 4. Write a function that receives as a parameters a list of musical notes (strings), a list of moves (integers) and a start position (integer). The function will return the song composed by going though the musical notes beginning with the start position and following the moves given as parameter.
# 	 Example : compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2) will return ["mi", "fa", "do", "sol", "re"]

def compose(notes, moves, start):
    res = [notes[start]]
    for move in moves:
        if(move > len(notes)):
            move = move % len(notes)
        if(move < -len(notes)):
            move = len(notes) - move % len(notes)
        start += move
        if start < 0:
            start += len(notes) - 1
        if start > len(notes):
            start -= len(notes)
        res.append(notes[start])
    else:
        return res


print(compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, -100], 2))


# 5. Write a function that receives as parameter a matrix and will return the matrix obtained by replacing all the elements under the main diagonal with 0 (zero).

def mainDiagonal(matrix):
    for i in range(0, len(matrix[0])):
        for j in range(0, len(matrix[0])):
            if i >= j:
                matrix[i][j] = 0
    else:
        print(matrix)


matrix = [[1, 2, 3, 4],
          [1, 2, 3, 4],
          [1, 2, 3, 4],
          [1, 2, 3, 4]]

mainDiagonal(matrix)


#  6. Write a function that receives as a parameter a variable number of lists and a whole number x. Return a list containing the items that appear exactly x times in the incoming lists.
# Example: For the [1,2,3], [2,3,4],[4,5,6], [4,1, "test"] and x = 2 lists [1,2,3 ] # 1 is in list 1 and 4, 2 is in list 1 and 2, 3 is in lists 1 and 2.


def xOccurences(x, *lists):
    res = []
    list = []
    for l in lists:
        list += l
    for item in list:
        if list.count(item) == x:
            res.append(item)
    else:
        return set(res)


print(xOccurences(2, [1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"]))



#   7. Write a function that receives as parameter a list of numbers (integers) and will return a tuple with 2 elements.
#   The first element of the tuple will be the number of palindrome numbers found in the list and the second element will be the greatest palindrome number.


def palindromeMaxPal(list):
    count = 0
    max = 0
    for number in list:
        if str(number) == str(number)[::-1]:
            count += 1
            if number > max:
                max = number
    else:
        return tuple([count, max])


print(palindromeMaxPal([10101,101,10001,221,32,100]))


#  8. Write a function that receives a number x, default value equal to 1, a list of strings, and a boolean flag set to True.
#  For each string, generate a list containing the characters that have the ASCII code divisible by x if the flag is set to True,
#  otherwise it should contain characters that have the ASCII code not divisible by x


def funct8(x, list, flag):
    res = []
    if flag:
        for string in list:
            tempRes = []
            for c in string:
                if ord(c) % x:
                    tempRes.append(c)
            else:
                res.append(tempRes)
    else:
        for string in list:
            tempRes = []
            for c in string:
                if not ord(c) % x:
                    tempRes.append(c)
            else:
                res.append(tempRes)
    return res


print(funct8(2, ["test", "hello", "lab002"], True))


# 9. Write a function that receives as paramer a matrix which represents the heights of the spectators in a stadium
#    and will return a list of tuples (line, column) each one representing a seat of a spectator which can't see the game.
#    A spectator can't see the game if there is at least one taller spectator standing in front of him.
#    All the seats are occupied. All the seats are at the same level. Row and column indexing starts from 0,
#    beginning with the closest row from the field.


def stadium(seats):
    res = []
    for col in range(0, len(seats[0])):
        maxHeight = 0
        for row in range(0, len(seats)):
            if seats[row][col] <= maxHeight:
                res.append(tuple([row, col]))
            else:
                maxHeight = seats[row][col]
    else:
        return res


field = [[1, 2, 3, 2, 1, 1],
        [2, 4, 4, 3, 7, 2],
        [5, 5, 2, 5, 6, 4],
        [6, 6, 7, 6, 7, 5]]

print(stadium(field))


# 10. Write a function that receives a variable number of lists and returns a list of tuples as follows:
# the first tuple contains the first items in the lists, the second element contains the items on the position 2 in the lists, etc.


def func10(*input_lists):
    res = []
    tuplel = max(len(x) for x in input_lists)
    for list in input_lists:
        if len(list) < tuplel:
            list.extend(None for i in range(len(list), tuplel))
    for i in range(0, tuplel):
        temp = []
        for j in range(0, len(input_lists)):
            temp.append(input_lists[j][i])
        else:
            res.append(temp)
    return res


print(func10([1, 2, 3], [5, 6, 7, 8], ["a", "b", "c"]))


# 11. Write a function that will order a list of string tuples based on the 3rd character of the 2nd element in the tuple.
# Example: ('abc', 'bcd'), ('abc', 'zza')] ==> [('abc', 'zza'), ('abc', 'bcd')]

def order(list):
    return sorted(list, key=lambda x: x[1][2])

print(order([('abc', 'bcd'), ('abc', 'zza')]))


#  12. Write a function that will receive a list of words  as parameter and will return a list of lists of words,
#  grouped by rhyme. Two words rhyme if both of them end with the same 2 letters.

def rhyme(words):
    res = []
    for index in range(0, len(words)):
        wordList = list(filter(lambda item: item[-2:] == words[index][-2:], words))
        # wordList = []
        # wordList.append(words[index])
        # for i in range (index+1, len(words)):
        #     if words[index][-2:] == words[i][-2:]:
        #         wordList.append(words[i])
        if not (wordList in res):
            res.append(wordList)
    return res


print(rhyme(['ana', 'banana', 'carte', 'arme', 'parte']))