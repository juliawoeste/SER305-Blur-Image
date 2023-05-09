from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image, ImageFilter
from tkinter.filedialog import askopenfilename, asksaveasfilename


""" Animate the original image (based on the current blur value - which would NEED to be stored or accessed!)"""
def animate():
    global original_image
    # Create list of frames for gif
    frames = []
    print(scaleVal)
    # Add frames going from original to blurred
    for i in range(0, scaleVal + 1, 5):
        blur_radius = i / 5
        blurred_image = original_image.filter(ImageFilter.BoxBlur(radius=blur_radius))
        frames.append(blurred_image)
    
    # Add frames going from blurred image to original image
    for i in range(scaleVal, -1, -5):
        blur_radius = i / 5
        blurred_image = original_image.filter(ImageFilter.BoxBlur(radius=blur_radius))
        frames.append(blurred_image)
    
    # Save frames as gif
    frames[0].save('blur_animation.gif', format='GIF', append_images=frames[1:], save_all=True, duration=50, loop=0)
    
    # Open gif in new window
    animation = tk.Toplevel(root)
    animation.title("Blurring Animation")
    animation.geometry("300x300")
    
    animation_label = tk.Label(animation)
    animation_label.pack()

    gif = Image.open('blur_animation.gif')
   
    animation_frames = []
    try:
        while True:
            animation_frames.append(ImageTk.PhotoImage(gif))
            gif.seek(gif.tell() + 1)
    except EOFError:
        pass
    
    def update_animation(frame_index):
        animation_label.config(image = animation_frames[frame_index])
        animation.after(50, update_animation, (frame_index + 1) % len(animation_frames))
        
    update_animation(0)
        
def save_image():
    file_type = [('Jpg files', '*.jpg')]
    filename = tk.filedialog.asksaveasfilename(filetypes = file_type, defaultextension='.jpg')
    if filename:
        # Convert image to RGB mode (keep getting RGB error if you don't do this)
        rgb_image = blurred_image.convert('RGB')
        rgb_image.save(filename)

    
""" Invoked when slider is moved. Blur the image based on the new value and update the displayed image."""
def slide_activate(v):
    global original_image
    global blurred_image
    global scaleVal
    scaleVal = int(v)
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
    original_image=original_image.convert('RGBA').resize((350,350)) 
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
root.geometry("800x600")

root.configure(bg='#062b66') #####


frame = Frame(root, width = 700, height = 500)

frame.configure(bg='#062b66') #####

photo = PhotoImage(file='download.png')

frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)
button = tk.Button(root, text = "Upload File",bd=0, pady=15,padx=100,foreground='black',font=('Sana',17),command = upload_file)
image_label = tk.Label(root)  # This will be used to display the image
original_imag = None # This variable will store the ORIGINAL image once loaded (keeping here so global scope)

#global scaleVal
global horizontal
horizontal = Scale(root, from_= 0, to= 100, resolution=10, orient=HORIZONTAL, length= 200,bd=3,background='black',foreground='white', command = slide_activate)
horizontal.pack(side = 'bottom')

button2 = Button(root, text = "Click to Animate the Image", bd=0,pady=10,padx=25,foreground='black',font=('Sana',14), command = animate)
button2.pack(side = 'bottom')

save_button = Button(root, text="Save Image", bd=0,pady=10,padx=25,foreground='black',font=('Sana',14), command=save_image)
save_button.pack(side='bottom')

    
#my_label = Label(root, text = "hello")

button.pack()

root.mainloop()