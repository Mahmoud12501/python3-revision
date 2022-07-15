from termcolor import colored

# BMI=weight (kg) /hight (m^2)
def BMI(weight,hight):
    bmi= float (weight  /hight )
    if bmi<=18.4:
        print(colored(f"BMI={bmi} and status: Underweight",'yellow'))
    elif bmi<=24.9 and bmi>=18.5:
        print(colored(f"BMI={bmi} and status: Normal",'green'))    
    elif bmi<=39.9 and bmi>=25:
        print(colored(f"BMI={bmi} and status: Overweight",'magenta'))    
    else:
        print(colored(f"BMI={bmi} and status: Obese",'red'))

BMI(57,2)