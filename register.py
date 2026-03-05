import tkinter as tk
from tkinter import messagebox

students = []

# Add student
def add_student():
    name = entry_name.get()
    age = entry_age.get()
    course = entry_course.get()

    if name == "" or age == "" or course == "":
        messagebox.showwarning("Input Error", "Please fill all fields")
        return

    student = {"name": name, "age": age, "course": course}
    students.append(student)
    list_students()

    clear_fields()

# List students
def list_students():
    listbox.delete(0, tk.END)
    for i, student in enumerate(students):
        text = f"{i+1}. {student['name']} | Age: {student['age']} | Course: {student['course']}"
        listbox.insert(tk.END, text)

# Delete student
def delete_student():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Selection Error", "Select a student to delete")
        return

    index = selected[0]
    students.pop(index)
    list_students()

# Load student for update
def select_student():
    selected = listbox.curselection()
    if not selected:
        return

    index = selected[0]
    student = students[index]

    entry_name.delete(0, tk.END)
    entry_name.insert(0, student["name"])

    entry_age.delete(0, tk.END)
    entry_age.insert(0, student["age"])

    entry_course.delete(0, tk.END)
    entry_course.insert(0, student["course"])

# Update student
def update_student():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Selection Error", "Select a student to update")
        return

    index = selected[0]

    students[index] = {
        "name": entry_name.get(),
        "age": entry_age.get(),
        "course": entry_course.get()
    }

    list_students()
    clear_fields()

# Clear fields
def clear_fields():
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_course.delete(0, tk.END)

# Exit program
def exit_program():
    window.destroy()

# Window
window = tk.Tk()
window.title("Student Registration System")
window.geometry("500x450")

title = tk.Label(window, text="Student Registration System", font=("Arial", 16))
title.pack(pady=10)

# Name
tk.Label(window, text="Student Name").pack()
entry_name = tk.Entry(window)
entry_name.pack()

# Age
tk.Label(window, text="Age").pack()
entry_age = tk.Entry(window)
entry_age.pack()

# Course
tk.Label(window, text="Course").pack()
entry_course = tk.Entry(window)
entry_course.pack()

# Buttons
frame_buttons = tk.Frame(window)
frame_buttons.pack(pady=10)

tk.Button(frame_buttons, text="Add Student", command=add_student).grid(row=0, column=0, padx=5)
tk.Button(frame_buttons, text="Update Student", command=update_student).grid(row=0, column=1, padx=5)
tk.Button(frame_buttons, text="Delete Student", command=delete_student).grid(row=0, column=2, padx=5)
tk.Button(frame_buttons, text="List Students", command=list_students).grid(row=0, column=3, padx=5)

# Listbox
listbox = tk.Listbox(window, width=60)
listbox.pack(pady=10)
listbox.bind("<<ListboxSelect>>", lambda event: select_student())

# Exit button
tk.Button(window, text="Exit Program", command=exit_program).pack(pady=10)

window.mainloop()