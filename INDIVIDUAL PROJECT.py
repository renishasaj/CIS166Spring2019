
# author: RENIS HASAJ
# Module: individual project 1
# date: 4/24/19



import tkinter as tk
from tkinter import messagebox


# Function that will be called when the "Convert" button is clicked.
# Converts weight in pounds to grams, kilograms and ounces.
def convert(pounds, grams, kilograms, ounces):
    try:
        # Try to convert string to float
        p = float(pounds.get())
    except:
        # If user entered value that can't be converted to float,
        # then show message stating that input is invalid and finish function.
        messagebox.showinfo("Invalid input", "Please enter a number under the entry")
        return None
    grams.config(text=str(p*453.59237))
    kilograms.config(text=str(p*453.59237/1000))
    ounces.config(text=str(p*16))
    
# Create window
window = tk.Tk()
window.title("Weight converter")
window.geometry('400x400')
window.configure(background='gray')

# Place text labels
tk.Label(window, text="Weight converter", font=('Arial black', 20), background='gray').place(x=70, y=50)
tk.Label(window, text="Grams", font=('Arial', 10), background='gray').place(x=76, y=160)
tk.Label(window, text="Kilograms", font=('Arial', 10), background='gray').place(x=76, y=220)
tk.Label(window, text="Ounces", font=('Arial', 10), background='gray').place(x=76, y=280)

# Place input field where user enter pounds
pounds = tk.Entry(window, width=18, font=('Arial black', 14))
pounds.place(x=70, y=100)
tk.Label(window, text="lb", font=('Arial black', 14), background='gray').place(x=310, y=100)

# Place labels that show converted weights
grams = tk.Label(window, text="0.0", font=('Arial', 10), width=28, anchor=tk.W, padx=6, borderwidth=1, relief="solid")
grams.place(x=70, y=185)
kilograms = tk.Label(window, text="0.0", font=('Arial', 10), width=28, anchor=tk.W, padx=6, borderwidth=1, relief="solid")
kilograms.place(x=70, y=245)
ounces = tk.Label(window, text="0.0", font=('Arial', 10), width=28, anchor=tk.W, padx=6, borderwidth=1, relief="solid")
ounces.place(x=70, y=305)

# Place "Convert" button
tk.Button(window, text="Convert", font=('Arial', 12),
          width=11, bg="#DD7733", fg='red',
          command=lambda:convert(pounds, grams, kilograms, ounces)).place(x=200, y=350)

# Start mainloop
window.mainloop()
