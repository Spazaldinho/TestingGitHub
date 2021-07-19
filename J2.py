maxName = ""
inputName = ""
maxBid = 0
inputBid = 0
N = input()

for x in range(int(N)):
    inputName = input()
    inputBid = int(input())

    if inputBid > maxBid:
        maxBid = inputBid
        maxName = inputName

print(maxName)
