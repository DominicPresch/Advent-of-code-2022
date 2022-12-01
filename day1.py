with open("C:\\Users\\Dominic Presch\\Desktop\\adventofcode\\day1.txt") as x:
    whale = 0
    largestwhale = 0
    secondlargestwhale = 0
    thirdlargestwhale = 0
    for inp in x:
        inp = inp.strip()
        if inp != "":
            whale += int(inp)
        else:
            if whale > largestwhale:
                thirdlargestwhale = secondlargestwhale
                secondlargestwhale = largestwhale
                largestwhale = whale
            elif whale > secondlargestwhale:
                thirdlargestwhale = secondlargestwhale
                secondlargestwhale = whale
            elif whale > thirdlargestwhale:
                thirdlargestwhale = whale
            whale = 0
    print(largestwhale + secondlargestwhale + thirdlargestwhale)
    ######the second largest whale would win in a fight#######