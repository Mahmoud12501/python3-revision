import datetime
import schedule
import time
from win10toast import ToastNotifier




remander_dict={}
def to_dolist():
    
    
    number_task=int(input("how mant task do you want to record: "))

    # take task and thier time 
    for i in range(number_task):
        task_time=input(f"entert task{i+1} time: ").split(":")
        task_name=input(f"task{i+1} name: ").title
    
        h,m=map(int,task_time)
        task_time=datetime.time(h,m,0,0)
        print(task_time)
        print(type(task_time))

        # store task name as a key in dict and time as a value
        remander_dict[task_name]=task_time  
        x=remander_dict[task_name]  
    
def rmander():  
    notvication=ToastNotifier() 

    for   task,not_time  in remander_dict.items():
        
        if not_time==datetime.datetime.now().time():
             print("yes")
             notvication.show_toast(
            task,
            f"Time of {task}",
            icon_path=None,
            duration=20,
            threaded=True)
        else:
            print(not_time)
            print(datetime.datetime.now().time())
            print("no")

to_dolist()
schedule.every(1).seconds.do(rmander)
while True:
 
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)
