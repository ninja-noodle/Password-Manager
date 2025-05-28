import tkinter as tk
from tkinter import messagebox

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("650x450")
        self.root.title("See what you've typed!")


        self.menubar = tk.Menu(self.root)

        self.file_menu = tk.Menu(self.menubar, tearoff=0)
        self.file_menu.add_command(label="Quit", command=self.on_closing)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Force Quit", command=exit)

        self.action_menu = tk.Menu(self.menubar, tearoff=0)
        self.action_menu.add_command(label="Show Message", command=self.show_message)
        self.action_menu.add_command(label="Clear Textbox", command=self.clear)

        self.menubar.add_cascade(menu=self.file_menu, label="File")
        self.menubar.add_cascade(menu=self.action_menu, label="Action")
        self.root.config(menu=self.menubar)


        self.label = tk.Label(self.root, text="Start typing...", font=("Monospace", 18))
        self.label.pack(padx=5, pady=10)


        self.text_box = tk.Text(self.root, height=5, font=("Monospace", 14))
        self.text_box.bind("<KeyPress>", self.shortcut)
        self.text_box.pack(padx=10, pady=10)

        self.check_state = tk.IntVar()
        self.checkbox = tk.Checkbutton(self.root, variable=self.check_state, text="Show in Messagebox", font=("Monospace", 14))
        self.checkbox.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text="Show Message", font=("Monospace", 16), command=self.show_message)
        self.button.pack(padx=10, pady=10)


        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()


    def show_message(self):
        if self.check_state.get() == 1:
            messagebox.showinfo(title="Message", message=self.text_box.get("1.0", tk.END))
        else:
            print(self.text_box.get("1.0", tk.END))

    def shortcut(self, event):
        # print(event)
        # print(event.keysym)
        # print(event.state)
        if event.keysym == "Return" and event.state == 20:
            self.show_message()

    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Are you sure you want to quit?"):
            self.root.destroy()

    def clear(self):
        self.text_box.delete("1.0", tk.END)

GUI()
