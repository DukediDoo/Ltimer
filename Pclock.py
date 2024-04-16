import time
import keyboard
import threading
while True:

    

    rule_table = list(range(1, 61))

    usr_timeofchoice = (input("What time do you want to be ur timer to be set at, format method: Minutes, 60 limit.: "))


    def commands():
        while True:




            chelp = "COMMANDS: 'RM' = remaining time, 'Q' = quit, 'ADD' = adds time "


            cRM = print(f"time left in seconds: {usrtoccalculated}\ntime left in minutes: {int(usrtoccalculated)}")


            print(chelp)


            
            usr_APP_input = input("What u wanna do bro, just do help please. ")



        


            if usr_APP_input == "help":



                print(chelp)



            elif usr_APP_input == "RM":

                print(cRM)
            elif usr_APP_input == "Q":
                print("Goodbye")
                break
            elif usr_APP_input == "add":
                print("test")

            

            
                



    if usr_timeofchoice.isdigit() not in rule_table:




         

        print("Not a number or too high of one. Selec a number in the range of 1-61 ")


    else:
        usr_output = print("\nTimer has started: type 'help' without ' to get more commands/options like 'remaining time' ")

        if usr_output == "help":



    

        
        
            usrtoccalc = int(usr_timeofchoice)



         
         
            usrtoccalculated =  usrtoccalc * int(60)


       

        

      
            while usrtoccalculated != 0:


                
                tsleep = time.sleep(60)




            
                usrtoccalculated -= 60

            
            
                print(f" A minute has passed, remaining time: {int(usrtoccalculated/60)} minutes ")
                

            


        




            
       




        





