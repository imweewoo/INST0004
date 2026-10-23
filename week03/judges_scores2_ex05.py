#Strictly Judges Program

#Find numerous low judge score
def lowScore(score):
    minJudge = [1]
    minScore = score[0]
    for i in range(1, len(score)):
        if score[i] < minScore:
            minScore = score[i]
            minJudge = [i + 1]
        elif score[i] == minScore:
            minJudge.append(i + 1)
    return minJudge

#Find numerous max judge 
def highScore(score):
    maxJudge = [1]
    maxScore = score[0]
    for i in range(1, len(score)):
        if score[i] > maxScore:
            maxScore = score[i]
            maxJudge = [i + 1]
        elif score[i] == maxScore:
            maxJudge.append(i + 1)

    return maxJudge

def main():
    #Initialisation + text
    judges = {}
    name = []
    score = []
    total = 0
    highest = []
    lowest = []

    print("Welcome to strictly come dancing :)")
    print("   *** The results are in ***   ")

    #Loop for Name and Score inputs
    for i in range(1,5):
        judgeName = input("Enter name of judge: ")

        #Score validation within required range
        while True:
            try:
                #Entry + check if month is >= 12
                judgeScore = int(input(f"Enter score[{i}]: "))
                if judgeScore < 1 or judgeScore > 10:
                    raise ValueError(f"The allowed score is between (1-10)")
                break
            except ValueError as error:
                #integer error message
                if "invalid literal" in str(error):
                    print("Enter an integer")
                else:
                    print(error)

        #Add to list
        name.append(judgeName)

        #Adjust dictionary judgeScore + total + lists
        if judgeScore < 5:
            judges[judgeName] = 5
            total = total + 5
            score.append(5)
        else:
            judges[judgeName] = judgeScore
            total = total + judgeScore
            score.append(judgeScore)

    #Find highest and lowest score
    highest = highScore(score)
    lowest = lowScore(score)

    #Output text
    print(judges)
    print("There are 4 judges.")
    print(f"The first judge, {name[0]}, gave: {score[0]}")
    print(f"The final judge, {name[3]}, gave: {score[3]}")

    #Output max and min judges
    for i in range(len(highest)):
        print(f"The judge with the highest score is: {name[highest[i] - 1]}")
    for i in range(len(lowest)):
        print(f"The judge with the lowest score is: {name[lowest[i] - 1]}")

    print(f"The total score is: {total}")

main()

