import tkinter as tk


def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)


def delete_task(event):
    try:
        selected_task = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task)
    except IndexError:
        pass


def exit_program():
    window.destroy()


window = tk.Tk()
window.title("Hernandez-ToDo")
window.geometry("400x400")

menu_bar = tk.Menu(window)

file_menu = tk.Menu(menu_bar, tearoff=0, bg="#2E86AB", fg="white")
file_menu.add_command(label="Exit", command=exit_program)
menu_bar.add_cascade(label="File", menu=file_menu)

window.config(menu=menu_bar)

label_title = tk.Label(
    window,
    text="To-Do List\nType a task and click Add Task.\nRight-click a task to delete it.",
    font=("Arial", 12)
)
label_title.pack(pady=10)

entry_task = tk.Entry(window, width=35)
entry_task.pack(pady=5)

button_add = tk.Button(
    window,
    text="Add Task",
    command=add_task,
    bg="#F18F01",
    fg="black"
)
button_add.pack(pady=5)

frame_tasks = tk.Frame(window)
frame_tasks.pack(pady=10)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks = tk.Listbox(
    frame_tasks,
    width=45,
    height=10,
    yscrollcommand=scrollbar_tasks.set
)
listbox_tasks.pack(side=tk.LEFT)

scrollbar_tasks.config(command=listbox_tasks.yview)

listbox_tasks.bind("<Button-3>", delete_task)

window.mainloop()