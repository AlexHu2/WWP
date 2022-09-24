
def calculateNeeded(inputCurrent, inputDesired, finalPercent):
    overallPercent = (100 - finalPercent)/100
    currentGrade = inputCurrent
    desiredGrade = inputDesired
    neededFinal = (desiredGrade - overallPercent * currentGrade)/(finalPercent/100)
    return neededFinal



inputCurrent = int(input("What is your current grade: "))
inputDesired = int(input("What is your desired grade: "))
finalPercent = float(input("What percent is your final worth: "))
print(calculateNeeded(inputCurrent, inputDesired, finalPercent))
