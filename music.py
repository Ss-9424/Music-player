from tkinter import *
import pygame
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title('Carvaan mp3 player')
root.iconbitmap('D:\Music player\music.ico')
root.geometry("500x300")
pygame.mixer.init()


def add_song():
    song=filedialog.askopenfilename(initialdir='Music player',title="Choose A Song",filetypes=(("mp3 Files","*.mp3"),))
    song=song.replace(".mp3","")
    song=song.replace("D:/Music player/",'')
    dj.insert(END,song)

def add_many_songs():
    songs=filedialog.askopenfilenames(initialdir='Music player',title="Choose A song",filetypes=(("mp3 Files","*.mp3"),))
    for song in songs:
        song=song.replace(".mp3","")
        song=song.replace("D:/Music player/",'')
        dj.insert(END,song)


def delete_song():
    dj.delete(ANCHOR)
    pygame.mixer.music.stop()

def delete_all_songs():
    dj.delete(0,END)
    pygame.mixer.music.stop()

def play():
    song=dj.get(ACTIVE) 
    song=f'D:/Music player/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)   


def stop():
    pygame.mixer.music.stop()
    dj.selection_clear(ACTIVE)

global paused
paused=False


def pause(is_paused):
    global paused
    paused=is_paused

    if paused:
        pygame.mixer.music.unpause() 
        paused=False  
    else:
        pygame.mixer.music.pause()
        paused=True

def next_song():
    next_one=dj.curselection()
    next_one=next_one[0]+1
    song=dj.get(next_one)        
    song=f'D:/Music player/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)   

    dj.selection_clear(0,END)

    dj.activate(next_one)

    dj.selection_set(next_one,last=None)

def previous_song():
    next_one=dj.curselection()
    next_one=next_one[0]-1
    song=dj.get(next_one)        
    song=f'D:/Music player/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)   

    dj.selection_clear(0,END)

    dj.activate(next_one)

    dj.selection_set(next_one,last=None)



dj=Listbox(root,bg="black",fg="green",width=60,selectbackground="gray",selectforeground="black")
dj.pack(pady=20)
back_btn_img=ImageTk.PhotoImage(file='p50.png')
play_btn_img=ImageTk.PhotoImage(file='play50.png')
pause_btn_img=ImageTk.PhotoImage(file='pause50.png')
stop_btn_img=ImageTk.PhotoImage(file='stop.png')
forward_btn_img=ImageTk.PhotoImage(file='knext.png')

controls_frame=Frame(root)
controls_frame.pack()


forward_btn=Button(controls_frame,image=forward_btn_img,borderwidth=0,command=next_song)
play_btn=Button(controls_frame,image=play_btn_img,borderwidth=0,command=play)
pause_btn=Button(controls_frame,image=pause_btn_img,borderwidth=0,command=lambda: pause(paused))
stop_btn=Button(controls_frame,image=stop_btn_img,borderwidth=0,command=stop)
back_btn=Button(controls_frame,image=back_btn_img,borderwidth=0,command=previous_song)

back_btn.grid(row=0,column=0,padx=10)
forward_btn.grid(row=0,column=4,padx=10)
play_btn.grid(row=0,column=1,padx=10)
pause_btn.grid(row=0,column=2,padx=10)
stop_btn.grid(row=0,column=3,padx=10)

my_menu=Menu(root)
root.config(menu=my_menu)

add_song_menu=Menu(my_menu)
my_menu.add_cascade(label="Add Songs",menu=add_song_menu)
add_song_menu.add_command(label="Add One song To Playlist",command=add_song)
add_song_menu.add_command(label="Add Many song To Playlist",command=add_many_songs)

remove_song_menu=Menu(my_menu)
my_menu.add_cascade(label="Remove Songs",menu=remove_song_menu)
remove_song_menu.add_command(label="Delete a song from Playlist",command=delete_song)
remove_song_menu.add_command(label="Delete a songs from Playlist",command=delete_all_songs)



root.mainloop()
