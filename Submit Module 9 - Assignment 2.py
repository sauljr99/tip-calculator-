#Source 1 ChatGPT
#Source 2 https://docs.python.org/3/library/tkinter.html
#Source 3 https://www.activestate.com/resources/quick-reads/how-to-create-a-calculator-in-python-tkinter/
#Source 4 https://www.geeksforgeeks.org/python/radiobutton-in-tkinter-python/

#lines 7 to 12 from class
import tkinter as tk #imports tkinter and rename it to tk for shorter code
from tkinter import messagebox #import the messagebox
root = tk.Tk() #create application window
root.title("Tip Calculator") #set window title
root.geometry("400x400") #set window size
root.resizable(False, False) #prevent user resizing window

#lines 16 Source 2
tip_var = tk.IntVar(value=15) #create an integer variable to store

#lines 18 from class
def calculate(): #function that runs when butten is clicked

    #Lines 22 to 29 ChatGPT Source 1
    try: #start error handling if user enters invalid input
        bill = float(bill_entry.get()) #bill amount entry box
        people = int(people_entry.get()) #people number entry box
    except ValueError: #run this block if the input cannot be converted to number
        messagebox.showerror("Error", "Enter valid numbers!") #show error to the user
        return #stop the fiunction so the rest of the calculation does not run
    tip = bill * (tip_var.get() / 100) #calculate the tip based on the selected percentage
    total = bill + tip #calculate the total amount including tip
    result_label.config(text=f"Tip: ${tip:.2f}   |   Total: ${total:.2f}   |   Each: ${total/people:.2f}", fg="#2ecc71") #update the result lable with calculated values in green

#lines 32 to 41 from class some from source 3
tk.Label(root, text="Tip Calculator", font=("Helvetica", 18, "bold"), fg="black").pack(pady=15) #title label at top
tk.Label(root, text="Bill Amount ($):", fg="black").pack() #lable for bill amount
bill_entry = tk.Entry(root, width=20, font=("Helvetica", 12), justify="center") #create as input box for bill amount
bill_entry.pack(pady=5) #place the bill entry box window
tk.Label(root, text="Number of People:", fg="black").pack() #add label asking number of people
people_entry = tk.Entry(root, width=20, font=("Helvetica", 12), justify="center") #create input box for number of people
people_entry.pack(pady=5) #place the people entry box on the window
tk.Label(root, text="Select Tip %:", fg="black").pack(pady=5) #add label for tip percentage section
tip_frame = tk.Frame(root) #create a frame to hold the radio buttons
tip_frame.pack() #place the frame in the window

#lines 44 to 45 source 4
for pct in [10, 15, 20, 25]: #loop through the tip percentage choices
    tk.Radiobutton(tip_frame, text=f"{pct}%", variable=tip_var, value=pct, font=("Helvetica", 11)).pack(side=tk.LEFT, padx=8) #create radio button for each tip option

#lines 48 from class and source 3
tk.Button(root, text="Calculate", command=calculate, font=("Helvetica", 11, "bold"), padx=15, pady=6).pack(pady=12) #create a button that calls calculate() when clicked

#lines 51 to 52 source 2 and source 3
result_label = tk.Label(root, text="", font=("Helvetica", 11, "bold")) #create an empty label to show the result
result_label.pack() #place the result label in the window

#lines 55 from class
root.mainloop() #start the tkinter event loop so the window stays open