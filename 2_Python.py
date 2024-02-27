def calculateHours(hours, rate):
    if hours <= 40:
        wage = hours * rate
        return wage
    else:
        wage = 40 * rate + (hours - 40) * rate * 1.2
        return wage
    
inputHours = int(input("Input hours: "))
inputRate = float(input("Input rate: "))

wage = calculateHours(inputHours, inputRate)

print("Wage: " + str(wage))
