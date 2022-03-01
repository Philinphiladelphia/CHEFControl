from tkinter import *
import cv2
from PIL import ImageTk, Image

from os import listdir
from os.path import isfile, join

RECIPE_PATH = "recipes"

root=Tk()
# add widgets here

def btn_func(args):
	print("hey")


def create_recipe_frame(container):
	frame = Frame(container, padx=20, pady= 10)

	inner_frame = Frame(frame, padx=20, pady= 10)
	inner_frame.grid(column=0, row=0, pady=10)

	recipes = [f for f in listdir(RECIPE_PATH) if isfile(join(RECIPE_PATH, f))]

	Label(inner_frame, text="Recipe Control", fg='Black', font=("Impact", 13)).grid(column=0, row=0, pady=10)

	default = StringVar(inner_frame)
	default.set(recipes[0])
	menu = OptionMenu(inner_frame, default, *recipes).grid(column=0, row=1, sticky=W)

	buttonframe = Frame(inner_frame)
	buttonframe.grid(column=0, row=2, sticky=W)
	buttonframe.columnconfigure(0, weight=2)
	buttonframe.columnconfigure(1, weight=2)

	Button(buttonframe, text='Start').grid(column=0, row=0, sticky=W)
	Button(buttonframe, text='Stop').grid(column=1, row=0, sticky=W, padx=5)

	Label(inner_frame, text="Output:", fg='Black', font=("Impact", 13)).grid(column=0, row=3, pady=10, sticky=W)

	outputtext = Text(inner_frame, height=10, width=15)
	outputtext.grid(column=0, row=4)

	Label(frame, text="Video Feed:", fg='Black', font=("Impact", 13)).grid(column=1, row=0, stick=N)
	lmain = Label(frame, width=400, height = 300)
	lmain.grid(column=1, row=0, sticky=E)

	cap = cv2.VideoCapture(0)
	def video_stream():
		_, frame = cap.read()
		cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
		img = Image.fromarray(cv2image)
		imgtk = ImageTk.PhotoImage(image=img)
		lmain.imgtk = imgtk
		lmain.configure(image=imgtk)
		lmain.after(1, video_stream) 

	video_stream()

	return frame

root.columnconfigure(0, weight=4)

Label(root, text="CHEF Interface", fg='Red', font=("Impact", 13)).grid(column=0, row=0, pady=10)

recipe_frame = create_recipe_frame(root)

recipe_frame.grid(column=0, row=1, sticky=W)



# btn=Button(root, text="This is Button widget", fg='blue')
# lbl.grid(column=0, row=0)

# btn.bind('<Button-1>', btn_func)


# txtfld=Entry(root, text="This is Entry Widget", bd=5)
# lbl.grid(column=0, row=0)

# v1 = IntVar()
# v2 = IntVar()
# C1 = Checkbutton(window, text = "Cricket", variable = v1)
# C2 = Checkbutton(window, text = "Tennis", variable = v2)
# C1.place(x=400, y=300)
# C2.place(x=400, y=350)

root.title('Hello Python')
root.geometry("610x500+10+20")
root.mainloop()