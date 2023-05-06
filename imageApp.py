from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image, ImageFilter
from tkinter.filedialog import askopenfilename

""" Animate the original image (based on the current blur value - which would NEED to be stored or accessed!)"""
def animate():
    print("ANIMATING!!!")

""" Invoked when slider is moved. Blur the image based on the new value and update the displayed image."""
def slide_activate(v):
    global original_image
    # TO DO: Check that an image has been selected - or else ignore (or report an error)
    # print("You have selected a blur value of " + v)
    v = int(v)/5 # Convert to integer (and scale it - way too blurry otherwise)
    blurred_image = original_image.filter(ImageFilter.BoxBlur(radius = v))
    set_image(blurred_image)

""" Upload an image file, set it to be the original image, and display it (unblurred). """    
def upload_file():
    global original_image
    file_type = [('Jpg files', '*.jpg'), ('PNG files', '*.png')]
    filename = tk.filedialog.askopenfilename(filetypes = file_type)
    original_image = Image.open(filename)
    original_image=original_image.convert('RGBA').resize((250,250)) 
    # Note. Had to convert to RGBA b/c there were issues with BoxBlur running on PNG files.
    # Could be more robust and only do this if image was PNG.
    set_image(original_image)

""" Set the displayed image to the given image img. """
def set_image(img):
    global image_label
    img = ImageTk.PhotoImage(img) # Convert image to TkInter PhotoImage

    image_label.image = img
    image_label['image'] = img
    image_label.pack()

root = tk.Tk()
root.title("Blur an Image!")
root.geometry("500x500")

frame = Frame(root, width = 600, height = 400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)
label = tk.Label(root, text = "upload a file")
button = tk.Button(root, text = "Upload File", width = 20, command = upload_file)
image_label = tk.Label(root)  # This will be used to display the image
original_imag = None # This variable will store the ORIGINAL image once loaded (keeping here so global scope)

horizontal = Scale(root, from_= 0, to= 100, orient=HORIZONTAL, length= 200, command = slide_activate)
horizontal.pack(side = 'bottom')
#horizontal.get()

button2 = Button(root, text = "Click to Animate the Image", bd = 5, command = animate)
button2.pack(side = 'bottom')
    
#my_label = Label(root, text = "hello")
label.pack()
button.pack()

root.mainloop()