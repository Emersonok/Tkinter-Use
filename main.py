from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(500, 300)
window.config(padx=20, pady=20) # create space around the program

def btn():
    my_input = input.get()
    my_label.config(text= my_input)
    print(my_input)

def btn2():
    new_input = input.get()
    new_label = Label(text=new_input, font=("Courier", 21, "italic" ))
    new_label.grid(column=3, row=4)
    new_label.config(padx=30, pady=30)


#label
my_label = Label(text="My Label", font=("Courier", 26, "bold"))
#my_label.pack() #my_label.pack(side=left, expand=True)
#my_label.place(x=0,y=0)
my_label.grid(column= 0,row= 0)

my_label["font"] = ("Arial")
my_label.config(text="Not First Anymore")

# Button
button = Button(text="Click", command=btn)
#button.pack() # .pack makes it stay on the screen
#button.place(x=20,y=20)
button.grid(column=1, row=1)

button2 = Button(text="send", command=btn2)
button2.grid(column=2, row=0)

#Entry
input = Entry(width=10)
#input.pack(side= "left")
#input.place(x=40,y=40)
input.grid(column=3, row= 3)










window.mainloop()