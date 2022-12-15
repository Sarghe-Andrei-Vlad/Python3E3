import utils
while True:
    inputs = input("Enter a number or q to quit: ")
    if inputs == "q":
        break
    inputs = int(inputs)
    utils.process_item(inputs)