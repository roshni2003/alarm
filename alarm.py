import datetime
from playsound import playsound
alarmhour= int(input("ENter hour:"))
alarmminute=int(input("Enter minute:"))
alarmAm=input("am/pm:")

if alarmAm=="pm":
    alarmhour+=12
    
while True:
    if alarmhour==datetime.datetime.now().hour and alarmminute==datetime.datetime.now().minute:
        print("playing..")
        playsound("nuclear.mp3") 
        break