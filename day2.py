with open("C:\\Users\\Dominic Presch\\Desktop\\adventofcode\\day2.txt") as x:
    total = 0
    for values in x:
        values = values.strip()
        letter1 = values[0]
        letter2 = values[2]
        match letter2:  #  A is rock, B is paper, C is scissors, X is lose, Y is draw, Z is win
            case "X":       #need to lose
                match letter1:
                    case "A":
                        total += 3
                    case "B":    
                        total += 1
                    case "C":
                        total += 2
            case "Y":       #tie
                match letter1:
                    case "A":
                        total += 4
                    case "B":
                        total += 5
                    case "C":
                        total += 6
            case "Z":       #win
                match letter1:
                    case "A":
                        total += 8
                    case "B":
                        total += 9
                    case "C":
                        total += 7
    print(total)
