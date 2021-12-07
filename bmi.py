def calc(*args):
    return args[0]/((args[1])/100)**2

def printbmi(bmi):
    if bmi <= 18.4:
        print("You are underweight.")
    elif bmi <= 24.9:
        print("You are healthy.")
    elif bmi <= 29.9:
        print("You are over weight.")
    elif bmi <= 34.9:
        print("You are severely over weight.")
    elif bmi <= 39.9:
        print("You are obese.")
    else:
        print("You are severely obese.")

if __name__ == "__main__":
    height = float(input("Enter height in cm: "))
    weight = float(input("Enter weight in kg: "))
    bmi = calc(weight, height)
    format_bmi = "{:.2f}".format(bmi)
    print("Your BMI is", format_bmi)
    printbmi(bmi)