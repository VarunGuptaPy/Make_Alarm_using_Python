import datetime
from playsound import playsound
def alarm():
    time = input("enter the time in  hour:min:second")

    while True:
        Time_Ac = datetime.datetime.now()
        now = Time_Ac.strftime("%H:%M:%S")
        if now == time:
            print("time to wake up sir")
            playsound("drum.wav")
alarm()