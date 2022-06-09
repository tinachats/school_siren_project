import datetime as dt
import schedule
import time
from pygame import mixer

# This is the main routine
def main():
    # School days: Monday == 0 and end on Friday == 4
    day = dt.datetime.today().weekday()
    
    while day:
        if day >= 0 and day <= 4:
            # Lessons start at 07:30
            start_time = '07:30'
            
            # Lessons end at 14:50 unless it's Friday
            end_time = '14:50'
            
            # Siren is to ring for 20 seconds straight
            schedule.every().day.at(start_time).do(siren, 20)
            schedule.every().day.at(end_time).do(siren, 20)
            
            # School in progress
            print('Lessons in progress...')
            
            while True:
                schedule.run_pending()
                time.sleep(1)
        else:
            print('Weekending...')
            
        time.sleep(5) 
        
def lesson_periods(now_time, start_time, end_time): 
    # During the day
    if start_time < end_time: 
        return now_time >= start_time and now_time <= end_time 
    else: 
        # Over midnight: 
        return now_time >= start_time or now_time <= end_time 
    
# Ringing and stopping the siren
def siren(sec):
    # Initialize the mixer
    mixer.init()
    
    # Load the siren sound into the mixer
    mixer.music.load('school-bell.mp3')
    
    # Ring the siren
    mixer.music.play()
    
    # Ring the siren for the entered seconds
    time.sleep(sec)
    
    # Stop the siren 
    mixer.music.stop()

# Executable code
if __name__ == '__main__':
    main()