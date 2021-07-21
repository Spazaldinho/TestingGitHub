listOfInstructions = []

while True:

    currentNumber = input()
    sum = int(currentNumber[0]) + int(currentNumber[1])

    if currentNumber == "99999":
        break
    elif sum == 0:
        msg = msg
    elif (sum % 2 == 0):
        msg = "right"
    else:
        msg = "left"

    inputMessage = msg + " " + currentNumber[2] + currentNumber[3] + currentNumber[4]
    listOfInstructions.append(inputMessage)
    
i = 0
length = int(len(listOfInstructions))

while i < length:
    print(listOfInstructions[i])
    i += 1
