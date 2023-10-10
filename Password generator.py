import math
#get word you're going to encrypt
website = input("Enter the name of the website you want a password for:")

#arrays containing all the characters
lowerChars=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upperChars=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbersSymbols=['1','2','3','4','5','6','7','8','9','0','!','_']

#get information from website name
def getLength():
    return(len(website))
def getLetters():
    global letterArray
    letterArray = []
    for i in website:
        letterArray.append(i)
    return(letterArray)
def getNumbers():
    global numberArray
    numberArray = []
    for i in website:
        numberArray.append(str(lowerChars.index(i)))
    return(numberArray)
def addNumbers():
    total = 0
    for i in range (0,len(numberArray)):
        num = int(numberArray[i])
        total += num
    return(total)
def oddEvenLetters():
    global oddLetterArray
    global evenLetterArray
    oddLetterArray = []
    evenLetterArray = []
    for i in range (0,len(letterArray)):
        if i%2 == 0:
            evenLetterArray.append(letterArray[i])
        elif i%2 != 0:
            oddLetterArray.append(letterArray[i])
    return(evenLetterArray, oddLetterArray)


#generate password
def genPass():
    #letter whos position in the alphabet is equal to the length of the website name +1
    passwordArray = []
    passwordArray.append(lowerChars[getLength()])

    #positions of all the numbers added together, through a bunch of math and 1 lower 1 upper 1 number from that
    def getFinalNumUpper():
        finalNum = math.ceil(((((((addNumbers()/3)+6)/7.2)*100000)+18)*97))
        while True:
            if finalNum > (len(upperChars)-1):
                finalNum = math.ceil(finalNum/3.1)
            elif finalNum < 0:
                finalNum = math.ceil(finalNum*2.1)
            else:
                break
        return upperChars[finalNum]
    
    def getFinalNumLower():
        finalNum = math.ceil(((((((addNumbers()/3)+6)/7.2)*100000)+18)*97))
        while True:
            if finalNum > (len(lowerChars)-1):
                finalNum = math.ceil(finalNum/3)
            elif finalNum < 0:
                finalNum = math.ceil(finalNum*2)
            else:
                break
        return lowerChars[finalNum]
    
    def getFinalNumNumber():
        finalNum = math.ceil(((((((addNumbers()/3)+6)/7.2)*100000)+18)*97))
        while True:
            if finalNum > (len(numbersSymbols)-1):
                finalNum = math.ceil(finalNum/3)
            elif finalNum < 0:
                finalNum = math.ceil(finalNum*2)
            else:
                break
        return numbersSymbols[finalNum]
    
    passwordArray.append(getFinalNumLower())
    passwordArray.append(getFinalNumUpper())
    passwordArray.append(getFinalNumNumber())

    #append odd letters
    for i in range(0,len(oddLetterArray)):
        if ((lowerChars.index(oddLetterArray[i]))%2) == 0:
            char = oddLetterArray[i].upper()
            passwordArray.append(char)
        else:
            char = oddLetterArray[i].lower()
            passwordArray.append(char)

    passwordArray.append(numberArray[1])
    
    return(passwordArray)

#call functions
getLength()
getLetters()
getNumbers()
addNumbers()
oddEvenLetters()
print("".join(genPass()))
