import datetime
import schedule
import time
from win10toast import ToastNotifier




remander_dict={}
# def to_dolist():
    
    
#     number_task=int(input("how mant task do you want to record: "))
#     for i in range(number_task):
#         task_time=input(f"entert task{i+1} time: ").split(":")
#         task_name=input(f"task{i+1} name: ").title
    
#         h,m=map(int,task_time)
#         task_time=datetime.time(h,m)
#         print(task_time)
#         print(type(task_time))
#         remander_dict[task_time]=task_name  
#         x=remander_dict[task_time]  
    
# def rmander():  
#     notvication=ToastNotifier() 
#     for not_time , task in remander_dict.items():
#         if not_time==datetime.datetime.now().time():
#              print("yes")
#              notvication.show_toast(
#             task,
#             f"Time of {task}",
#             icon_path=None,
#             duration=10,
#             threaded=True)
#         else:
#             print("no")

# schedule.every(1).seconds.do(rmander)
# while True:
 
#     # Checks whether a scheduled task
#     # is pending to run or not
#     schedule.run_pending()
#     time.sleep(1)


all_reminder=[]
def take_task():
    number_task=int(input("how mant task do you want to record: "))
    for i in range(number_task):
        all_reminder.append([])

        task_time=input(f"entert task{i+1} time: ").split(":")
        task_name=input(f"task{i+1} name: ").title()
            
        h,m=map(int,task_time)
        task_time=datetime.time(h,m)
        for j in range(1):
            all_reminder[i].append(task_time)
            all_reminder[i].append(task_name)
        
def rmander():  
    notvication=ToastNotifier() 
    tim = time.localtime()

    current_time = time.strftime("%H:%M:%S", tim)
    for i in all_reminder:
        # x=all_reminder[i][0]
        # print(x)
        if datetime.datetime.now().hour==datetime.datetime.now().hour:
             print("yes")
             notvication.show_toast(
            all_reminder[i][1],
            f"Time of { all_reminder[i][1]}",
            icon_path=None,
            duration=10,
            threaded=True)
        else:
            print("no")

take_task()
schedule.every(1).seconds.do(rmander)
while True:
 
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)

