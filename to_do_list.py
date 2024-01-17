from tkinter import *
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(END, task)
        entry.delete(0, END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def clear():
    entry.delete(0, END)

def clear_all():
    listbox.delete(0, END)

def update_task():
    selected_task_index = listbox.curselection()
  
    if selected_task_index:
        updated_task = entry.get()
        if updated_task:
            listbox.delete(selected_task_index)
            listbox.insert(selected_task_index[0], updated_task)
            entry.delete(0, END)
        else:
            messagebox.showwarning("Warning", "Please enter an updated task.")
    else:
        messagebox.showwarning("Warning", "Please select a task to update.")

# Create the main window
root = Tk()
root.title("To-Do List")
root.geometry("700x660")
root.resizable(0, 0)
root.configure(bg="black")

# note frame
note = Frame(root, bg="black")
note.pack(side=TOP, pady=10)

ent = Label(note, text='Enter Task', font=('cambria', 18, 'bold', 'italic'), width=35, bg='black', fg="white")
ent.grid(row=1, column=0, padx=5, pady=5)
entry = Entry(note, font=('cambria', 22, 'bold'), bd=5, width=40, bg='gray25', fg="white")
entry.grid(row=2, column=0, padx=5, pady=5)

# button frame
btn_fr = Frame(root, bg="black")
btn_fr.pack(pady=10)

add_button = Button(btn_fr, font=('cambria', 14,'bold'), text='Add Task', width=11, bg="dark turquoise", fg='azure', command=add_task)
add_button.grid(row=1, column=1, pady=5)

delete_button = Button(btn_fr, font=('cambria', 14,'bold'), text="Delete Task", width=11, bg="dark turquoise", fg='azure', command=delete_task)
delete_button.grid(row=1, column=2, pady=5)

update_button = Button(btn_fr, font=('cambria', 14,'bold'), text="Update Task", width=11, bg="dark turquoise", fg='azure', command=update_task)
update_button.grid(row=1, column=3, pady=5)

clear_button = Button(btn_fr, font=('cambria', 14,'bold'), text="Clear task", width=11, bg="dark turquoise", fg='azure', command=clear)
clear_button.grid(row=1, column=4, pady=5)

clear_button = Button(btn_fr, font=('cambria', 14,'bold'), text="Clear list", width=11, bg="dark turquoise", fg='azure', command=clear_all)
clear_button.grid(row=1, column=5, pady=5)


# Create a frame for the listbox
list_frame = Frame(root, bg="black")
list_frame.pack(side=BOTTOM, pady=10)

list_label = Label(list_frame, text='NOTES', font=('cambria', 18, 'bold', 'italic'), width=40, bg='black', fg="white")
list_label.pack(padx=5, pady=5)

listbox = Listbox(list_frame, font=('cambria', 18), selectmode=SINGLE, width=110, height=100, bg='gray30', fg="white")
listbox.pack()

root.mainloop()
