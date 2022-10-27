# 1.Write a function that receives as parameters two lists a and b and returns a list of sets containing:
#   (a intersected with b, a reunited with b, a - b, b - a)

def setList(a, b):
    a_int_b = set(a) & set(b)
    a_reu_b = set(a) | set(b)
    a_min_b = set(a) - set(b)
    b_min_a = set(b) - set(a)
    res = [a_int_b, a_reu_b, a_min_b, b_min_a]
    return res


print("Ex1: ", setList([1, 2, 3, 4, 5], [0, 2, 4, 6, 8]))


# 2. Write a function that receives a string as a parameter and returns a dictionary in which the keys are the
# characters in the character string and the values are the number of occurrences of that character in the given
# text. Example: For string "Ana has apples." given as a parameter the function will return the dictionary: {'a': 3,
# 's': 2, '.': 1, 'e': 1, 'h': 1, 'l': 1, 'p': 2, ' ': 2, 'A': 1, 'n': 1} .

def charDictionary(inputString):
    myDictionary = dict()
    # inputString = inputString.lower()

    for char in inputString:
        if myDictionary.get(char) is None:
            myDictionary[char] = 1
        else:
            myDictionary[char] += 1

    return myDictionary


print("Ex2: ", charDictionary('Ana has apples'))


# 3. Compare two dictionaries without using the operator "==" returning True or False.
#    (Attention, dictionaries must be recursively covered because they can contain other containers,
#    such as dictionaries, lists, sets, etc.)

def dictionaryCompare(A, B):
    if A.keys() != B.keys():
        return False

    for key in A.keys():
        if type(A[key]) == dict:
            if not dictionaryCompare(A[key], B[key]):
                return False
        elif type(A[key]) == tuple or type(A[key]) == set:
            if not dictionaryCompare(A[key], B[key]):
                return False
        elif A[key] != B[key]:
            return False

    return True


print("Ex3: ", dictionaryCompare({'Ana': 5, 'has': 3, 'apples': 1}, {'Ana': 5, 'has': 3, 'apples': 1}))


# 4. The build_xml_element function receives the following parameters: tag, content, and key-value elements
#    given as name-parameters. Build and return a string that represents the corresponding XML element.
#    Example: build_xml_element ("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid ")
#    returns  the string = "<a href=\"http://python.org \ "_class = \" my-link \ "id = \" someid \ "> Hello there </a>"

def build_xml_element(tag, content, **dataPairs):
    res = '<'
    res += tag
    for key in dataPairs:
        res += key + '=\ "' + dataPairs[key] + '"\ '
    res += '> ' + content + '</' + tag + '>'

    return res


print("Ex4: ", build_xml_element("a", "Hello there", href=" http://python.org ", _class=" my-link ", id=" someid "))


# 5. The validate_dict function that receives as a parameter a set of tuples ( that represents validation rules
#    for a dictionary that has strings as keys and values) and a dictionary. A rule is defined as follows:
#    (key, "prefix", "middle", "suffix"). A value is considered valid if it starts with "prefix", "middle" is inside the value
#    (not at the beginning or end) and ends with "suffix".
#    The function will return True if the given dictionary matches all the rules, False otherwise.
#    Example: the rules  s={("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}  and
#    d= {"key1": "come inside, it's too cold out", "key3": "this is not valid"} =>
#    False because although the rules are respected for "key1" and "key2" "key3" that does not appear in the rules.

def validate_dict(rules, dictionary):
    keyNr = []
    for rule in rules:
        keyNr.append(rule[0])

    for key in dictionary:
        if key not in keyNr:
            print('keyNrRule not found')
            return False

    for key in dictionary:
        keyNr = [x for x in rules if x[0] == key]
        if not dictionary[key].startswith(keyNr[0][1]):
            return False
        if not dictionary[key].endswith(keyNr[0][3]):
            return False
        if keyNr[0][2] != "":
            if dictionary[key].find(keyNr[0][2]) == -1 or \
                    dictionary[key].find(keyNr[0][2]) == 0 or \
                    dictionary[key].find(keyNr[0][2]) >= len(dictionary[key]) - len(keyNr[0][2]):
                return False

    return True


print("Ex5: ", validate_dict({("key1", "", "inside", ""), ("key2", "", "", "valid")},
                             {"key1": "come inside, it's too cold out", "key2": "this is not valid"}))


# 6. Write a function that receives as a parameter a list and returns a tuple (a, b),
#    representing the number of unique elements in the list, and b representing the number of duplicate elements in the list
#    (use sets to achieve this objective).

def listElementCount(input):
    return len(set(input)), len(input) - len(set(input))


print("Ex6: ", listElementCount(['Ana', 'Maria', 'Ana', 'Mircea']))


# 7. Write a function that receives a variable number of sets and returns a dictionary with the following operations
#    from all sets two by two: reunion, intersection, a-b, b-a. The key will have the following form: "a op b",
#    where a and b are two sets, and op is the applied operator: |, &, -.

def operationalDictionary(*inputSet):
    res = dict([])
    for i in range(0, len(inputSet)):
        j = i + 1
        while j < len(inputSet):
            res[str(inputSet[i]) + " | " + str(inputSet[j])] = inputSet[i] | inputSet[j]
            res[str(inputSet[i]) + " & " + str(inputSet[j])] = inputSet[i] & inputSet[j]
            res[str(inputSet[i]) + " - " + str(inputSet[j])] = inputSet[i] - inputSet[j]
            res[str(inputSet[j]) + " - " + str(inputSet[i])] = inputSet[j] - inputSet[i]
            j += 1

    return res


print("Ex7: ", operationalDictionary({1, 2}, {2, 3}))


# 8. Write a function that receives a single dict parameter named mapping.
# This dictionary always contains a string key "start". Starting with the value of this key you must obtain a list of objects
# by iterating over mapping in the following way: the value of the current key is the key for the next value,
# until you find a loop (a key that was visited before).
# The function must return the list of objects obtained as previously described.
# Ex: loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'})
# will return ['a', '6', 'z', '2']

def findLoop(mapping):
    loop = []
    step = mapping.get('start')
    loop.append(step)
    while True:
        if mapping.get(step) is None:
            return 'No loop available'
        if mapping.get(step) in loop:
            return loop
        step = mapping.get(step)
        loop.append(step)


print("Ex8: ", findLoop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))


# 9. Write a function that receives a variable number of positional arguments and a variable number of keyword arguments
# adn will return the number of positional arguments whose values can be found among keyword arguments values.
# Ex: my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5) will return returna 3

def findArgs(*posArgs, **keyArgs):
    count = 0
    for val in posArgs:
        if val in keyArgs.values():
            count += 1
    return count


print("Ex9: ", findArgs(1, 2, 3, 4, x=1, y=2, z=3, w=5))
