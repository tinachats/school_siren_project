# Import the datetime and time modules
import datetime
import schedule
import time

# Count down timer function taking time in minutes
def count_down_timer(period):
    # Entered timer should be in minutes
    period = int(period * 60)
    while period:
        min, sec = divmod(period, 60)
        timer = '{:02d}:{:02d}'.format(min, sec)
        print(timer, end='\r')
        time.sleep(1)
        period -= 1
        
    # Play and stop the siren
    siren()
    
# Siren function to play and stop the siren
def siren():
    # Import the pygame module to play 
    # and stop the audio file
    from pygame import mixer
    
    # Initialize the mixer
    mixer.init()
    
    # Load the audio file
    mixer.music.load('assets/school-bell-sound.mp3')
    
    # Start playing the audio file
    mixer.music.play()
    print('The siren is ringing.')
    
# Main module
def main():
    # Make the lessons start at 07:30 everyday
    schedule.every().day.at('12:52').do(siren)
    now = datetime.datetime.now()
    hour = now.hour
    min = now.minute
    count_down_timer(1)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
    
# Executable function
if __name__ == '__main__':
    main()
        