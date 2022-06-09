import time

# Sound siren function
def sound_siren():
    print('Siren is ringing...')

# This is the main program
def lesson_time(period):
    period = int(period * 60)
    while period:
        min, sec = divmod(period, 60)
        timer = '{:02d}:{:02d}'.format(min, sec)
        print(timer, end="\r")
        time.sleep(1)
        period -= 1
    sound_siren()
             
# Lunchtime
def lunchtime():
    print('This is lunchtime....')
    
# Hometime
def hometime():
    print('This is hometime...')
    
    
# Call main
def main():
    # this code runs 24 hours
    end_time = 24
    
    time = 0
    
    while time < end_time:
        print(time)
        time += 1
        
        if time < 13:
            lesson_time(1)
        elif time == 13:
            lunchtime()
        elif time >= 15:
                hometime()
        else:
            lesson_time(1)
            
main()
            
            

        