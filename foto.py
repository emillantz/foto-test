import time
import os
import subprocess as bash
path = "/home/emill/Bilder/"

#set cwd
os.chdir(path)
prevsize = len(os.listdir())

#start slideshow
bash.run(["feh --auto-zoom --fullscreen --hide-pointer --slideshow-delay 5 --reload 20" + path + " &"], shell=True) 
while True:
    dir = os.listdir()
    dir.sort()
    #if image is added, start a temp slide with the newest images
    if(len(dir) > prevsize):
        print("reached if statement")
        strlist = ""
        for i in range(len(dir) - prevsize):
            strlist += dir[prevsize + i]
        print(strlist)
        bash.run(["feh --auto-zoom --fullscreen --hide-pointer --slideshow-delay 5 --on-last-slide=quit " + strlist], shell=True)
        ######
    prevsize = len(dir)
    time.sleep(20)
    print(len(dir))