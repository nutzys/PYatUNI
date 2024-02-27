inputHrs = input("Input hours: ")
inputRate = input("Input rate: ")

try:
    wage = inputHrs * inputRate
    print("Wage" + str(wage))
except:
    print("Enter a numeric value!")