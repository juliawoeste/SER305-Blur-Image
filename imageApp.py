from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image, ImageFilter
from tkinter.filedialog import askopenfilename


root = tk.Tk()
root.title("Blur an Image!")

root.geometry("500x500")
frame = Frame(root, width = 600, height = 400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)
label = tk.Label(root, text = "upload a file")
button = tk.Button(root, text = "Upload File", width = 20, command=lambda:upload_file())
def upload_file():
    file_type = [('Jpg files', '*.jpg'), ('PNG files', '*.png')]
    filename = tk.filedialog.askopenfilename(filetypes = file_type)
    img = Image.open(filename)
    img=img.resize((250,250))
    img = ImageTk.PhotoImage(img)
    e1 = tk.Label(root)
    e1.image = img
    e1['image'] = img
    e1.pack()
    
horizontal = Scale(root, from_= 0, to= 100, orient=HORIZONTAL, length= 200)
horizontal.pack(side = 'bottom')
#horizontal.get()

button2 = Button(root, text = "Click to Animate the Image", bd = 5)

button2.pack(side = 'bottom')


    
#my_label = Label(root, text = "hello")
label.pack()
button.pack()

root.mainloop()