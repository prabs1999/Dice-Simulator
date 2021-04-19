import tkinter as tk
from PIL import Image, ImageTk
import random

#adding​ images
dice=["face1.png","face2.png","face3.png","face4.png","face5.png","face6.png"]

root=tk.Tk()
root.title("Dice simulator")
root.geometry("600x400")
root.configure(bg='pink')

#label​
l1=tk.Label(root,text="enjoy the game!",fg="red",bg="black",font="Times 18 italic ")
l1.pack()
img = ImageTk.PhotoImage(Image.open(random.choice(dice)))

#Image​ label
l2=tk.Label(root,image=img)
l2.image=img
l2.pack(fill='none')

def roll():
    img = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    l2.configure(image=img)
    l2.image = img


#button​
button = tk.Button(root, text='Roll the Dice', fg='blue', command=roll)
button.pack()

root.mainloop()
