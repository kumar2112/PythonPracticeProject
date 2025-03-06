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

displayLable = ' * '*len(word)
sc = Label(app, text=displayLable, font='lucida 8 bold ').pack( 
      anchor=E, padx=200, pady=5) 

def on_key_pressed(event):
   entered_char = userv.get()

    # Update the label with the entered character
   sc.config(text=f"Character Entered: {entered_char}")
   # print("Char Entered")
   # # char = userv.get().lower()
   # # if char in word:
   # #    new_display = list(displayLable)
   # #    for i, c in enumerate(word):
   # #       if c == char:
   # #          new_display[i * 3 + 1] = char
   # #    displayLable = ''.join(new_display)
   # #    sc.config(text=displayLable)
   # # else:
   # #    count += 1
      
   # # userv.set('')






def gameBoard() :
   
   app.title("Word Guessing game") 
   app.geometry("500x500") 
   app.minsize(500, 500) 
   app.maxsize(600, 600) 
   
   heading = Label(text='Word Guessing Game', font="Helvicta 16 bold", bg='red', fg='green', padx=170).pack() 
   
   
 
   
   
   footer = Label(text=f'Developed by Praveen Kumar Jha',  font="Helvicta 8 bold", 
               bg='black', fg='tomato', padx=153).pack(side=BOTTOM)
 
  

gameBoard()  

app.mainloop()


