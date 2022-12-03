with open("C:\\Users\\Dominic Presch\\Desktop\\adventofcode\\day3.txt") as x:
    crebs = 0
    dicktionary = []
    listoflines = [gottem for gottem in x]
    for r in range(0,len(listoflines),3):
        #print(int((len(crabs)-1)/2))
        flag = False
        line1 = listoflines[r]
        line2 = listoflines[r+1]
        line3 = listoflines[r+2]
        for y in line1:
            for z in line2:
                if z == y:
                    for k in line3:
                        if y == z == k:
                            dicktionary.append(z)
                            flag = True
                            break
                if flag:
                    break
            if flag:
                break

        
    for p in dicktionary:
        if p.islower():
            crebs += ord(p) - 96
        else:
            crebs += ord(p) - 38    
        
    print(crebs)