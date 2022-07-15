from datetime import datetime


dob=input("What is your date of birth dd-mm-yyyy? ").split('-')

def age_calculator(birthdate):
    d,m,y=map(int,birthdate)
    birthdate=datetime(y,m,d)

    return f"you have {datetime.now().year-birthdate.year} years old"


def birthday_calculator(birthdate):
     d,m,y=map(int,birthdate)
     birthdate=datetime(datetime.now().year,m,d)

    #  check if birthdate > current day to avoid nigtave value 
     if birthdate<datetime.now():
        year=int(datetime.now().year)+1
        birthdate=datetime(year,m,d)

     return f"days left to your birthda is {(birthdate-datetime.now()).days}"

def main():
    choise=int(input("1-age_calculator\t2-how many days left to the birthday : "))
    if choise==1:
        print(age_calculator(dob))
    elif choise==2:
        print(birthday_calculator(dob))

if __name__=='__main__':
   main()