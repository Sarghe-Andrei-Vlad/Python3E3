def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True

def process_item(x):
    x = int(x)
    if x < 2:
        x = 3
    if x % 2 == 0:
        x += 1
    while not is_prime(x):
        x += 2
    print("The least prime number greater that your input is: ", x)

if __name__ == "__main__":
    print("salut")