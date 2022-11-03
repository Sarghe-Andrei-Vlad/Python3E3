# 1)	Să se scrie o funcție ce primeste un singur parametru, director, ce reprezintă calea către un director.
# Funcția returnează o listă cu extensiile unice sortate crescator (in ordine alfabetica) a fișierelor din
# directorul dat ca parametru.
# Mențiune: extensia fișierului ‘fisier.txt’ este ‘txt’
import os
import sys


def Ex1(path):
    extensions = set()
    try:
        if not os.path.dirname(path):
            raise NotADirectoryError()
    except NotADirectoryError:
        print("ex1: Given path is not a directory: " + path)
    else:
        for (root, dirs, files) in os.walk(path):
            for file_name in files:
                extensions.add(file_name.split('.')[-1])

    return sorted(extensions)


print("Ex1: ", Ex1("D:\Facultate\An3Sem1\ML\companion-lab-master"))


# 2)	Să se scrie o funcție ce primește ca argumente două căi: director si fișier.
# Implementati functia astfel încât în fișierul de la calea fișier să fie scrisă pe câte o linie,
# calea absolută a fiecărui fișier din interiorul directorului de la calea folder, ce incepe cu litera A.

def Ex2(director_path, file_path):
    try:
        if not os.path.dirname(director_path):
            raise NotADirectoryError()
        if not os.path.isfile(file_path):
            raise FileNotFoundError()
        file = open(file_path, 'wt')
    except NotADirectoryError:
        print("ex2: Given path is not a directory: " + director_path)
    except FileNotFoundError:
        print("ex2: Given path is not a file: " + file_path)
    except OSError:
        print("ex2: Unable to open the file: " + file_path)
    else:
        for (root, dirs, files) in os.walk(director_path):
            for file_name in files:
                if file_name.split('.')[0].startswith('L'):
                    file.write(director_path + '\\' + file_name + '\n')
        file.close()


# print("Ex2: ", Ex2("D:\Facultate\An3Sem1\ML\companion-lab-master","D:\Facultate\An3Sem1\Python3E3\Lab4\Ex2.txt"))

# 3) Să se scrie o funcție ce primește ca parametru un string my_path.
# Dacă parametrul reprezintă calea către un fișier, se vor returna ultimele 20 de caractere din conținutul fișierului.
# Dacă parametrul reprezintă calea către un director, se va returna o listă de tuple (extensie, count),
# sortată descrescător după count, unde extensie reprezintă extensie de fișier,
# iar count - numărul de fișiere cu acea extensie. Lista se obține din toate fișierele (recursiv) din directorul dat ca parametru.

def Ex3(my_path):
    try:
        if not os.path.dirname(my_path):
            raise ValueError()
    except ValueError:
        return "Given path is neither a directory or a file"
    else:
        if os.path.isfile(my_path):
            try:
                f = open(my_path, 'rt')
                res = f.read()
                return res[-20:]
            except OSError:
                return "Unable to open the file: " + my_path
        else:
            counter = []
            for (root, dirs, files) in os.walk(my_path):
                for file_name in files:
                    if len(counter) == 0:
                        aux = tuple((file_name.split('.')[-1], 1))
                        counter += tuple([aux])
                    elif file_name.split('.')[-1] in [x[0] for x in counter]:
                        for extension in counter:
                            if extension[0] == file_name.split('.')[-1]:
                                new_tuple = tuple((file_name.split('.')[-1], extension[1] + 1))
                                del counter[counter.index((file_name.split('.')[-1], extension[1]))]
                                counter += tuple([new_tuple])
                    else:
                        aux = tuple((file_name.split('.')[-1], 1))
                        counter += tuple([aux])

            return sorted(counter, reverse=True, key=lambda x: x[1])


print("Ex3: ", Ex3("D:\Facultate\An3Sem1\ML\companion-lab-master"))


# 4)	Să se scrie o funcție ce returnează o listă cu extensiile unice a fișierelor din directorul dat ca argument
# la linia de comandă (nerecursiv). Lista trebuie să fie sortată crescător.
# Mențiune: extensia fișierului ‘fisier.txt’ este ‘txt’, iar ‘fisier’ nu are extensie,
# deci nu va apărea în lista finală.

def Ex4():
    extensions = set()
    path = input()
    try:
        if not os.path.dirname(path):
            raise ValueError()
    except ValueError:
        return "Given path is neither a directory or a file"
    else:
        for file in os.listdir(path):
            if os.path.isfile(os.path.join(path + '\\', file)):
                extensions.add(file.split('.')[-1])
        return sorted(extensions)


print("Ex4: ", Ex4())

# 5)Să se scrie o funcție care primește ca argumente două șiruri de caractere, target și to_search și
# returneaza o listă de fișiere care conțin to_search. Fișierele se vor căuta astfel:
# dacă target este un fișier, se caută doar in fișierul respectiv iar dacă este un director se va căuta recursiv
# in toate fișierele din acel director. Dacă target nu este nici fișier, nici director, se va arunca
# o excepție de tipul ValueError cu un mesaj corespunzator.

def Ex5(target, to_search):
    try:
        if not os.path.isfile(target) and not os.path.isdir(target):
            raise ValueError()
    except ValueError:
        return "ex5: 'target' is not a file or a directory: " + target
    else:
        if os.path.isfile(target):
            fp = open(target, 'r')
            content = fp.read()
            fp.close()
            if content.find(to_search):
                return "ex5: to_search exists in file"
            else:
                return "ex5: to_search does not exists in file"
        else:
            find_files = []
            for (root, directories, files) in os.walk(target):
                for file in files:
                    file_path = os.path.join(root, file)
                    try:
                        fp = open(file_path, 'r')
                        content = fp.read()
                        fp.close()
                        if content.find(to_search):
                            find_files.append(file_path.split('.')[0])
                    except OSError as e:
                        print("Ex5: Unable to open the file: " + file)
                        print(e)
            return find_files


print("Ex5: ", Ex5("D:\Facultate\An2Sem1\CDC\Teme", "month"))
print("Ex5: ", Ex5("D:\Facultate\An3Sem1\ML\companion-lab-master\Lab2-Exercises.ipynb", "month"))