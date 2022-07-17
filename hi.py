import datetime
import schedule
import time
from win10toast import ToastNotifier

remander_dict={}
def to_dolist():
    
    
    number_task=int(input("how mant task do you want to record: "))
    for i in range(number_task):
        task_time=input(f"entert task{i+1} time: ").split(":")
        task_name=input(f"task{i+1} name: ").title
    
        h,m=map(int,task_time)
        task_time=datetime.time(h,m)
        print(task_time)
        print(type(task_time))
        remander_dict[task_time]=task_name  
    print(remander_dict)     
    
def rmander():  
    notvication=ToastNotifier() 
    for not_time , task in remander_dict.items():
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

to_dolist()
schedule.every(1).seconds.do(rmander)
while True:
 
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)

# x=datetime.time(2,3)
# print(x)
# y="hi".title()
# dict1={y:x}
# print(dict1)
