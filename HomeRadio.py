from tkinter import *
import os
import random
import pygame




path = os.getcwd()
path = path + "\mp3"
#print (path)
song = []
pygame.init()
pygame.mixer.init()






obj = os.scandir(path)

for entry in obj:
    if entry.is_file():
        
        if entry.name.lower().endswith('.mp3') :
           
            new = path+"\\"+entry.name
            song.append(new)

def play():
      pygame.mixer.music.unpause()
      
def pause():
      pygame.mixer.music.pause()

def Next():
        nowplay = random.choice(song)
        pygame.mixer.music.load(nowplay)

        name = nowplay.replace(path+"\\" , '')
        print(name)
        tkWindow.title(name)
        pygame.mixer.music.play()

          




tkWindow = Tk()  
tkWindow.geometry('245x35')  
tkWindow.title('Home Radio')
Next()



def check_event():
    for event in pygame.event.get():
        if event.type == MUSIC_END:
           Next() 
    tkWindow.after(100,check_event)

MUSIC_END = pygame.USEREVENT+1
pygame.mixer.music.set_endevent(MUSIC_END)


check_event() 







button = Button(tkWindow, width=7, height=1, font="Helvetica", text="Play", command=play, bg="lightblue", fg="black").grid(row=2,column=0)
button2 = Button(tkWindow, width=7, height=1, font="Helvetica", text="Pause", command=pause, bg="lightblue", fg="black").grid(row=2,column=1)
button3 = Button(tkWindow, width=7, height=1, font="Helvetica", text="Next", command=Next, bg="lightblue", fg="black").grid(row=2,column=2)

tkWindow.mainloop()
