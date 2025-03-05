import tkinter as tk
from tkinter import messagebox

# Function to check login credentials and open new window
def check_login():
    username = username_entry.get()
    password = password_entry.get()
    
    # Hardcoded credentials (you can modify this part as needed)
    correct_username = "admin"
    correct_password = "password123"
    
    if username == correct_username and password == correct_password:
        messagebox.showinfo("Login Successful", "Welcome to the system!")
        open_program_window()  # Open the next program window
        root.destroy()  # Close the login window after successful login
    else:
        messagebox.showerror("Login Failed", "Incorrect username or password!")

# Function to open the new program window after successful login
def open_program_window():
    # New window
    program_window = tk.Tk()
    program_window.title("Program Window")
    program_window.geometry("400x400")
    program_window.config(bg="#2E2E2E")
    
    # Label for the program window
    program_label = tk.Label(program_window, text="Welcome to the Program!", font=("Helvetica", 24), fg="#ffffff", bg="#2E2E2E")
    program_label.pack(pady=50)
    
    # Example of a simple program functionality
    button_action = tk.Button(program_window, text="Click Me!", font=("Helvetica", 14), fg="#ffffff", bg="#4CAF50", relief="solid", bd=2, command=button_action_func)
    button_action.pack(pady=20)
    
    # Run the new window
    program_window.mainloop()

# Function for button action in the new program window
def button_action_func():
    messagebox.showinfo("Action", "You clicked the button! Performing some action...")

# Creating the main window (Login Page)
root = tk.Tk()
root.title("Login Page")
root.geometry("400x400")
root.config(bg="#2E2E2E")

# Adding a frame for the login form
frame = tk.Frame(root, bg="#333333", bd=10, relief="solid", padx=20, pady=20)
frame.place(relx=0.5, rely=0.5, anchor="center")

# Adding a title label
title_label = tk.Label(frame, text="Login", font=("Helvetica", 24), fg="#ffffff", bg="#333333")
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# Username label and entry
username_label = tk.Label(frame, text="Username:", font=("Helvetica", 14), fg="#ffffff", bg="#333333")
username_label.grid(row=1, column=0, sticky="e", pady=5)

username_entry = tk.Entry(frame, font=("Helvetica", 14), fg="#333333", bg="#ffffff", bd=2, relief="solid")
username_entry.grid(row=1, column=1, pady=5)

# Password label and entry
password_label = tk.Label(frame, text="Password:", font=("Helvetica", 14), fg="#ffffff", bg="#333333")
password_label.grid(row=2, column=0, sticky="e", pady=5)

password_entry = tk.Entry(frame, font=("Helvetica", 14), fg="#333333", bg="#ffffff", bd=2, relief="solid", show="*")
password_entry.grid(row=2, column=1, pady=5)

# Login button
login_button = tk.Button(frame, text="Login", font=("Helvetica", 14), fg="#ffffff", bg="#4CAF50", relief="solid", bd=2, command=check_login)
login_button.grid(row=3, column=0, columnspan=2, pady=20)

# Styling the button on hover (optional)
def on_enter(e):
    login_button.config(bg="#45a049")

def on_leave(e):
    login_button.config(bg="#4CAF50")

login_button.bind("<Enter>", on_enter)
login_button.bind("<Leave>", on_leave)

# Run the application
root.mainloop()
