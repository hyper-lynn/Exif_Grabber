import os
import piexif
from Color_Console import *
from pyfiglet import Figlet 
import shutil
import keyboard
import sys
import exifread
import time


#header function 

try:

    #check cmd

    def body():
                
        computer_name = os.environ['COMPUTERNAME']  

        fix = "Exif_Grabber@" +computer_name + " > "

        #print("\n<----------Type help for more cmds---------->")

        cmds = input(fix)
        
        

        if cmds == "help":
            print("""

                    help \ ? \t\t\t-Help

                    start\t\t\t-grab the exif data in photo

                    save\t\t\t-save data in txt file

                    del\t\t\t\t-delete exif data 

                    exit\t\t\t-exit from the program
                """)
                    

            body()
                
                
        elif cmds == "?":
           print("""

                    help \ ? \t\t\t-Help

                    start\t\t\t-grab the exif data in photo

                    save\t\t\t-save data in txt file

                    del\t\t\t\t-delete exif data 

                    exit\t\t\t-exit from the program
                """)
           body()
                    
        elif cmds == "start":

            try:
#shwo exif metadata in photo
                photo = input("Enter Your Photo Name: ")

                f = open(photo, 'rb')

                tags = exifread.process_file(f)
                
                print("Exif Data of %s"%photo)
                
                for key in tags:
                    
                    value=tags[key]
                    
                    if key not in ['JPEGThumbnail']:
                            
                            print("....................................................................................\n")
                            
                            print(str(key),str(value))
                        
                print("")   
                

            except FileNotFoundError:

                print("\nImage Not Found!")
        

            body()

        elif (cmds == "save"):
            

            try:

                file_name = input("Enter Your txt_file name: ")

                photo = input("Enter Your Photo Name: ")

                f = open(photo, 'rb')

                tags = exifread.process_file(f)

                for key in tags:

                    value=tags[key]

                    if key not in ['JPEGThumbnail']:

                        table.rows.append([str(key) ,str(value)])

                        file = open(file_name, 'w')
                        print("<-------Grabbing %s"%photo + "------->",file = file)
                        print(table, file = file)
                       
                print("Successfully Save As %s"%file_name)
                print("/n")       

                body()
                        
                        
                

            except FileNotFoundError:

                print("\nImage Not Found!")
            

            body()

        elif cmds == "del":
            photo = input("Enter Your Phtoto name: ")

            #data = piexif.load(photo) # Dict with metadata
            piexif.remove(photo)
            empty = piexif.load(photo) # No metadata
            print("\n Successfully Remove Metadata in %s"%photo)

            body()


        elif cmds == "exit":
            print("\nBye!See you soon.")
            time.sleep(1)
            sys.exit()

        else:

            print("\nWrong Input!")

            body()
                

    def header():

        keyboard.press('f11')


        ''' change color ''' 


        hackerMan()


        ''' Use Figlet'''


        header = Figlet(font='slant')


        exif = '!!!!Exif Grabber!!!!'

        name = header.renderText(exif)


        print(name.center(shutil.get_terminal_size().columns))
        


        version = "Beta version,"


        global developer


        developer = "Developed by hyper-lynn"


        v_d = version + developer


        print(v_d.center(shutil.get_terminal_size().columns))
        print("\n")
        print("cmd = 'help' for more details\n")
        
        

        body()
        input()


    header()

#keyboardInterrput
except KeyboardInterrupt:


        print("\nBye....!See you Soon")   
        
        time.sleep(1)

        sys.exit()
