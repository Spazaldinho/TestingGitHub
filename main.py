listOfInstructions = []

while True:

    msg = "left"

    currentNumber = input()
    sum = int(currentNumber[0]) + int(currentNumber[1])
    print(sum)

    if currentNumber == "99999":
        break
    elif sum % 2 == 0:
        msg = "right"

    inputMessage = msg + " " + currentNumber[2] + currentNumber[3] + currentNumber[4]
    listOfInstructions.append(inputMessage)
    
i = 0
length = int(len(listOfInstructions))

while i < length:
    print(listOfInstructions[i])
    i += 1
