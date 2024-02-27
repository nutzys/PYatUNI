def calculateHours(hours, rate):
    wage = hours * rate
    return wage

inputHours = int(input("Enter hours:"))
inputRate = int(input("Enter rate:"))

wage = calculateHours(inputHours, inputRate)

print("Wage: " + str(wage))

