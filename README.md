#importing module as Required 
import customtkinter
from tkinter import*
from tkinter import messagebox

app = customtkinter.CTk()
app.title('To-Do List App')
app.geometry('350x450')
app.config(bg='Brown')


font1 = ('Arial',30,'bold')
font2 = ('Arial',18,'bold')
font3 = ('Arial',10,'bold')

#Add task function

def add_task():
    task = task_entry.get()
    if task:
        tasks_list.insert(0,task)
        task_entry.delete(0,END)
        save_tasks()
    else:
        messagebox.showerror('Error','Enter a task')    


#Add remove task()

def remove_task():
    selected = tasks_list.curselection()
    if selected:
        tasks_list.delete(selected[0])
        save_tasks()
    else:
        messagebox.showerror('Error','Choose a task to delete')

#Add Save tasks function

def save_tasks():
    with open("tasks.txt","w") as f:
        tasks = tasks_list.get(0,END)
        for task in tasks:
            f.write(task + "\n")   


#Adding task function 

def load_tasks():

    try:
        with open("tasks.txt","r") as f:
           tasks = f.readlines()
           for task in tasks:
               tasks_list.insert(0,task.strip())
    except FileNotFoundError:
        pass  

#App window Vision

title_label = customtkinter.CTkLabel(app,font=font1,text='To-Do List App',text_color='#fff',bg_color='Brown')
title_label.place(x=70 ,y=20)

add_button = customtkinter.CTkButton(app,command=add_task,font=font2,text_color='#fff',text='Add Task',fg_color='#06911f',hover_color='#06911f',bg_color='Blue',cursor='hand2',corner_radius=5,width=120)
add_button.place(x=40 ,y=80)

remove_button = customtkinter.CTkButton(app,command=remove_task,font=font2,text_color='#fff',text='Remove Task',fg_color='#96061c',hover_color='#96061c',bg_color='#09112e',cursor='hand2',corner_radius=5)
remove_button.place(x=180 ,y=80)

task_entry = customtkinter.CTkEntry(app,font=font2,text_color='#000',fg_color='#fff',border_color='#fff',width=280)
task_entry.place(x=40 ,y=120)

tasks_list = Listbox(app,width=50,height=20,font=font3)
tasks_list.place(x=48,y=200)

load_tasks()

app.mainloop()
