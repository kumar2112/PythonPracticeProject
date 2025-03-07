from tkinter import *
from PIL import ImageTk, Image 
import random 
import tkinter.messagebox as tmsg 

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

word = random.choice(words)

app = Tk() 
count = 0

userv = StringVar() 
user = Entry(app, textvariable=userv, justify=CENTER, relief=FLAT, borderwidth=2, font='Helvicta 18 bold')
user.pack(pady=10)

n = len(word)
repeated_list = ['*'] * n
displayLable = "".join(repeated_list)
sc = Label(app, text=displayLable, font='lucida 8 bold ')
sc.pack(anchor=E, padx=200, pady=5) 

k =n

def on_key_pressed(event):
   global k
   entered_char = userv.get()
   
   if entered_char in word :
        repeated_list[n-k]=entered_char
        k -=1
        print(k)
        
        
        sc.config(text="".join(repeated_list))
   
user.bind('<KeyPress>',on_key_pressed)




def gameBoard() :
   
   app.title("Word Guessing game") 
   app.geometry("500x500") 
   app.minsize(500, 500) 
   app.maxsize(600, 600) 
   
   heading = Label(text='Word Guessing Game', font="Helvicta 16 bold", bg='red', fg='green', padx=170).pack() 
   footer = Label(text=f'Developed by Praveen Kumar Jha',  font="Helvicta 8 bold", bg='black', fg='tomato', padx=153).pack(side=BOTTOM)
 
  

gameBoard()  

app.mainloop()


