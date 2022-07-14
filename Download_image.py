import requests
import shutil

img_url=input("enter imge url to download: ")
image_name=input("enter imge name: ")+".jpg"

img=requests.get(img_url,stream=True)

if img.status_code==200:

   with open(image_name,'wb') as f:
    shutil.copyfileobj(img.raw,f)
    print("success download ^_^")
else:
   print("oh no Error -_-")
