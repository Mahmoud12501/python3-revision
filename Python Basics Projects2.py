import datetime

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
  return round((f-32)/1.8000,5)


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




def main():
    # choice=input('enter choise:')
    # if
    print(convert_Fahrenheit_to_Celcius(1))
    countdown_calculator()
    print(email_slicer())
    currency_converter()




if __name__=='__main__':
    main()