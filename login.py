import tkinter as tk
from tkinter import messagebox
import os

# Predefined credentials (username and password)
correct_username = "zxcv"
correct_password = "vcxz"

# Function to check login credentials
def check_login():
    username = entry_username.get()
    password = entry_password.get()

    # Check if the username and password match
    if username == correct_username and password == correct_password:
        messagebox.showinfo("Login Success", "Welcome to the system!")
        open_task_selection()  # Open the task selection window after successful login
        root.destroy()  # Close the login window
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

# Function to open the task selection window
def open_task_selection():
    # Create a new window (task selection window)
    task_window = tk.Tk()
    task_window.title("Select a Task")
    task_window.geometry("400x300")

    # Label for instructions
    label = tk.Label(task_window, text="Please select a task to perform:", font=("Arial", 14))
    label.pack(pady=20)

    # Task options
    tasks = ["File Operations", "Simple Calculator", "Text Manipulation", "Task List Manager"]

    # Function to handle task selection
    def task_selected(task):
        if task == "File Operations":
            file_operations()
        elif task == "Simple Calculator":
            simple_calculator()
        elif task == "Text Manipulation":
            text_manipulation()
        elif task == "Task List Manager":
            task_list_manager()
        task_window.destroy()

    # Create a listbox with task options
    task_listbox = tk.Listbox(task_window, height=6, width=30, font=("Arial", 12))
    for task in tasks:
        task_listbox.insert(tk.END, task)  # Insert each task into the listbox
    task_listbox.pack(pady=20)

    # Button to confirm task selection
    select_button = tk.Button(task_window, text="Select Task", command=lambda: task_selected(task_listbox.get(tk.ACTIVE)))
    select_button.pack(pady=10)

    # Run the task selection window event loop
    task_window.mainloop()

# Function to perform File Operations (list, create, delete files)
def file_operations():
    def list_files():
        folder = entry_folder.get()
        if os.path.isdir(folder):
            files = os.listdir(folder)
            messagebox.showinfo("Files", "\n".join(files))
        else:
            messagebox.showerror("Error", "Invalid folder path!")

    def create_file():
        filename = entry_filename.get()
        content = entry_content.get()
        folder_path = entry_folder.get()
        
        # Create the file with the specified path and content
        if not os.path.isdir(folder_path):
            messagebox.showerror("Error", "Invalid folder path!")
            return
        
        file_path = os.path.join(folder_path, filename)
        
        try:
            with open(file_path, 'w') as file:
                file.write(content)
            messagebox.showinfo("Success", f"File '{filename}' created successfully at {folder_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create file: {e}")

    def delete_file():
        filename = entry_filename.get()
        folder_path = entry_folder.get()
        file_path = os.path.join(folder_path, filename)
        
        if os.path.exists(file_path):
            os.remove(file_path)
            messagebox.showinfo("Success", f"File '{filename}' deleted successfully!")
        else:
            messagebox.showerror("Error", "File not found!")

    # File operation window
    file_window = tk.Tk()
    file_window.title("File Operations")
    file_window.geometry("500x400")

    label = tk.Label(file_window, text="Select an operation:", font=("Arial", 14))
    label.pack(pady=20)

    label_folder = tk.Label(file_window, text="Folder Path:")
    label_folder.pack(pady=5)
    entry_folder = tk.Entry(file_window, width=40)
    entry_folder.pack(pady=5)

    label_filename = tk.Label(file_window, text="File Name:")
    label_filename.pack(pady=5)
    entry_filename = tk.Entry(file_window, width=40)
    entry_filename.pack(pady=5)

    label_content = tk.Label(file_window, text="Content (for creating file):")
    label_content.pack(pady=5)
    entry_content = tk.Entry(file_window, width=40)
    entry_content.pack(pady=5)

    # Buttons for file operations
    list_button = tk.Button(file_window, text="List Files in Directory", command=list_files)
    list_button.pack(pady=5)

    create_button = tk.Button(file_window, text="Create File", command=create_file)
    create_button.pack(pady=5)

    delete_button = tk.Button(file_window, text="Delete File", command=delete_file)
    delete_button.pack(pady=5)

    # Run the file operation window event loop
    file_window.mainloop()

# Function to perform simple calculator operations
def simple_calculator():
    def calculate():
        try:
            result = eval(entry_expression.get())  # Evaluate the mathematical expression
            messagebox.showinfo("Result", f"The result is: {result}")
        except Exception as e:
            messagebox.showerror("Error", f"Invalid expression: {e}")

    calculator_window = tk.Tk()
    calculator_window.title("Simple Calculator")
    calculator_window.geometry("400x300")

    label = tk.Label(calculator_window, text="Enter a mathematical expression:", font=("Arial", 14))
    label.pack(pady=20)

    entry_expression = tk.Entry(calculator_window, width=20, font=("Arial", 14))
    entry_expression.pack(pady=20)

    calculate_button = tk.Button(calculator_window, text="Calculate", command=calculate)
    calculate_button.pack(pady=20)

    # Run the calculator window event loop
    calculator_window.mainloop()

# Function to manipulate text (reverse text, count words)
def text_manipulation():
    def reverse_text():
        input_text = entry_input_text.get()
        reversed_text = input_text[::-1]
        messagebox.showinfo("Reversed Text", f"Reversed Text: {reversed_text}")

    def count_words():
        input_text = entry_input_text.get()
        word_count = len(input_text.split())
        messagebox.showinfo("Word Count", f"Word Count: {word_count}")

    text_window = tk.Tk()
    text_window.title("Text Manipulation")
    text_window.geometry("400x300")

    label = tk.Label(text_window, text="Enter text for manipulation:", font=("Arial", 14))
    label.pack(pady=20)

    entry_input_text = tk.Entry(text_window, width=40)
    entry_input_text.pack(pady=20)

    reverse_button = tk.Button(text_window, text="Reverse Text", command=reverse_text)
    reverse_button.pack(pady=5)

    count_button = tk.Button(text_window, text="Count Words", command=count_words)
    count_button.pack(pady=5)

    # Run the text manipulation window event loop
    text_window.mainloop()

# Function to manage tasks (view, add, delete tasks)
def task_list_manager():
    task_list = []

    def add_task():
        task = entry_task.get()
        task_list.append(task)
        messagebox.showinfo("Task Added", f"Task '{task}' added!")

    def view_tasks():
        tasks = "\n".join(task_list)
        messagebox.showinfo("Task List", tasks if tasks else "No tasks available.")

    def delete_task():
        task = entry_task.get()
        if task in task_list:
            task_list.remove(task)
            messagebox.showinfo("Task Deleted", f"Task '{task}' deleted!")
        else:
            messagebox.showerror("Error", "Task not found.")

    task_window = tk.Tk()
    task_window.title("Task List Manager")
    task_window.geometry("400x300")

    label = tk.Label(task_window, text="Enter a task:", font=("Arial", 14))
    label.pack(pady=20)

    entry_task = tk.Entry(task_window, width=30)
    entry_task.pack(pady=10)

    add_button = tk.Button(task_window, text="Add Task", command=add_task)
    add_button.pack(pady=5)

    view_button = tk.Button(task_window, text="View Tasks", command=view_tasks)
    view_button.pack(pady=5)

    delete_button = tk.Button(task_window, text="Delete Task", command=delete_task)
    delete_button.pack(pady=5)

    # Run the task manager window event loop
    task_window.mainloop()

# Create the main login window
root = tk.Tk()
root.title("Login Page")
root.geometry("300x200")  # Window size (width x height)

# Create and place the username label and entry field
label_username = tk.Label(root, text="Username:")
label_username.pack(pady=10)  # Add some space around the label
entry_username = tk.Entry(root)
entry_username.pack()

# Create and place the password label and entry field
label_password = tk.Label(root, text="Password:")
label_password.pack(pady=10)
entry_password = tk.Entry(root, show="*")  # 'show' hides the password text with asterisks
entry_password.pack()

# Create and place the login button
login_button = tk.Button(root, text="Login", command=check_login)
login_button.pack(pady=20)

# Run the Tkinter event loop to display the login window
root.mainloop()





