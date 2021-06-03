from tkinter import *
from pytube import YouTube
#main window
root = Tk()
root.geometry('500x300')
root.resizable(0,0)
#app title
root.title("YouTube video downloader" )
root.configure(background = "skyblue")
Label(root,text= "YouTube video downloader" , font="Luckiest-Guy 25 bold").pack()
#enter link from user
link = StringVar()
Label(root ,text="paste link here " , bd= 2,  font="Luckiest-Guy 15 bold").place(x=160 , y=60) 
linl_enter = Entry(width=70 , textvariable=link).place( x=32 , y=90)
#function to downloAD VIDEO
def downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root,text= 'download' ,font='Luckiest-Guy 15 bold ').place(x=180 , y=210)
    
#button to apply for downloding
Button(text='DOWNLOAD' , font=  'Luckiest-Guy 15 bold', bd=2 , bg='skyblue' , padx=2 , command=downloader).place(x=180,y=150)
root.mainloop()