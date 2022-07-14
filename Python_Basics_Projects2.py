import datetime
import string
import random
from win10toast import ToastNotifier
import schedule
import time

# Build a countdown calculator. Write some code that can take two dates as input,
# and then calculate the amount of time between them
def countdown_calculator():
    date1=input('enter date d-m-y: ').split('-')
    date2=input('enter date d-m-y: ').split('-')
    
    d1,m1,y1=map(int,date1)
    d2,m2,y2=map(int,date2)

    date1=datetime.datetime(y1,m1,d1)
    date2=datetime.datetime(y2,m2,d2)
    date_between=(date1-date2)
    print(date_between) 
    

# Build an email slicer
def email_slicer():
    end_username=0
    email=input("enter your email: ")

    email=email.split('@')
    user_name=email[0]
    domain_name=email[1]
    domain_name= domain_name.removesuffix('.com')
    return f"uesername is : {user_name} and domain of the email is: {domain_name}"


# convert Fahrenheit to Celcius
def convert_Fahrenheit_to_Celcius(f):
  return f"{round((f-32)/1.8000,5)} celsius"


def currency_converter():
    currency= input('''choise your Currency 
                        1>Dollar
                        2>Eg pound
                        3>Real saudi  ''')
    amount=int(input("enter The amount of money to be transferred: "))
    
    if currency=='1':
        print(f"{amount} dolar to egy pound ={amount*18.81:.3f}",f"{amount} dollar to Real saudi ={amount*3.75:.3f}",sep='\n')
    elif currency=='2':
        print(f"{amount} Eg pound to Dollar ={amount*0.053:.3f}",f"{amount} Eg pound  to Real saudi ={amount*0.20:.3f}",sep='\n')
    elif currency=='3':
        print(f"{amount} Real saudi  to Dollar ={amount*0.27:.3f}",f"{amount} Real saudi   to Eg pound ={amount*5.01:.3f}",sep='\n')


def generate_password(len_pass,no_uper,no_spcial,no_digt):
    #char form
    pass_char=list(string.ascii_uppercase)
    pass_digt=list(string.digits)
    pass_spcial=list("!@#$%^&*()_+?" )
    characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

    #random characters
    random.shuffle(pass_char)
    random.shuffle(pass_digt)
    random.shuffle(pass_spcial)
    
    # Calculating the number of charters that user want to be in password
    # check the total length with characters sum count
    characters_count=no_digt+no_spcial+no_uper
    if characters_count >len_pass:
        print("Characters total count is greater than the password length -_-")
    else:
        password=[]
        for c in range(no_uper):
            password.append(random.choice(pass_char))
        
        for c in range(no_spcial):
            password.append(random.choice(pass_spcial))
        
        for c in range(no_digt):
            password.append(random.choice(pass_digt))

        # if the total characters count is less than the password length
	    # add random characters to make it equal to the length
        if characters_count<len_pass:
            for c in range(len_pass-characters_count):
             password.append(random.choice(characters))

        random.shuffle(password)
        print(f"password: {''.join(password)}")
        
def to_dolist():
    global remander_list
    remander_list={}
    number_task=int(input("how mant task do you want to record: "))
    for i in range(number_task):
        task_time=input(f"entert task{i} time: ").split(":")
        task_name=input(f"task{i} name: ").title
        
        h,m=map(int,task_time)
        task_time=datetime.time(h,m)
       
        remander_list[task_time]=task_name  
    print(remander_list)     
    
def rmander():  
    notvication=ToastNotifier() 
    for not_time , task in remander_list.items():
        if not_time==datetime.datetime.now().time():
             print("yes")
             notvication.show_toast(
            task,
            f"Time of {task}",
            icon_path=None,
            duration=10,
            threaded=True)
        else:
            print("no")
            

def main():
    # choice=input('enter choise:')
    # if
    degree=int(input("enter degree fahrenheit: "))
    print(convert_Fahrenheit_to_Celcius(degree))
    print(12*"-")
    countdown_calculator()
    print(12*"-")
    print(email_slicer())
    print(12*"-")
    currency_converter()
    print(12*"-")
    generate_password(7,1,1,4)
    to_dolist()
    ######

    #######


# if __name__=='__main__':
#     main()
 
to_dolist()
schedule.every(1).seconds.do(rmander)
while True:
 
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)