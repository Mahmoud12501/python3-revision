import time
import schedule
import pyautogui
from datetime import datetime

def take_sceen():
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(f'Desktop\img\capture{datetime.now().minute}.png')  #write your path location here and name of imge with extention
    print("done")


schedule.every(1).seconds.do(take_sceen)
while True:
 
   
    schedule.run_pending()
    time.sleep(1)