import time
import keyboard
import threading
import tkinter
import webbrowser
from tkinter import *
from tkinter import ttk
from tkinter import font
from playsound import playsound
from pathlib import Path
import os

def timer():
    while True:
        rule_table = list(range(1, 61))
        usr_timeofchoice = (input("What time do you want to be ur timer to be set at, format method: Minutes, 60 limit.: "))
        
        if usr_timeofchoice.isdigit() and int(usr_timeofchoice) in rule_table:
            print("Timer has started: type 'help' without ' to get more commands/options like 'remaining time' ")
            usrtoccalc = int(usr_timeofchoice)
            usrtoccalculated = usrtoccalc * 60
            second_tracker = 0
            
            while usrtoccalculated != 0:
                
                time.sleep(1)
                usrtoccalculated -= 1
                

                second_tracker += 1
                #was for debugh# print(second_tracker)
                
                # Update the global variable with the remaining time
                global remaining_time
                remaining_time = usrtoccalculated

                if second_tracker == 60:
                    second_tracker = 0


                    
                    rmtimeprintf1 = print(f" A minute has passed, remaining time: {int(usrtoccalculated/60)} minutes {usrtoccalculated%60} seconds ") #bruh it cant print the global remainign_time bc it dont exist until time sleep happened cuz it dont exist until after 6 secs the change has been made and stored. LOL        else:
                if usrtoccalculated == 0:

                    
                    webbrowser.open('https://www.youtube.com/watch?v=3dfLtQxc3BY')
                    webbrowser.open('https://www.youtube.com/watch?v=qjqhy73yTq0') #Good job!
                    print("BEEEP BEEP TIMER DONE\nWant to set a new timer? Press Any Button to continue\nContinue? \n")
                    
        else:
            print("Not a number or too high of one.\n")

        

def commands():
    global remaining_time
    
    while True:
        chelp = "COMMANDS: 'RM' = remaining time, 'Q' = quit, 'ADD' = adds time "
        user_input = input("\n\n\nEnter a command: ")
        
        if user_input == "help":
            print(chelp)
        elif user_input == "RM":
            print(f"Remaining time: {int(remaining_time/60)} minutes {remaining_time%60} seconds")
        elif user_input.lower() == "q":
            print("Good bye! \n JUST KIDDING THIS THIS ONLY EXITS U FROM USING COMMANDS ;D ")
            break
        else:
            print("Invalid command. Type 'help' to see the available commands.")

timer_thread_obj = threading.Thread(target=timer)
input_thread_obj = threading.Thread(target=commands)

timer_thread_obj.start()
input_thread_obj.start()

# Wait for the threads to finish
timer_thread_obj.join()
input_thread_obj.join()

        




            
       




        





