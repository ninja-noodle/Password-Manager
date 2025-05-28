import tkinter as tk

root = tk.Tk()
root.title("Password Manager")
root.geometry("650x450")

label = tk.Label(root, text="Welcome", font=("Inter", 20, "bold"))
label.pack(padx=10, pady=10)

# text_input = tk.Text(root, height=3, font=("Inter", 10, "bold"))
# text_input.pack(padx=10)
#
# entry = tk.Entry(root)
# entry.pack(padx=10)
#
# button = tk.Button(root, text="Submit", font=("Inter", 10, "bold"))
# button.pack(padx=10, pady=10)

# _lb = label
# _in = input

input_frame = tk.Frame(root)
input_frame.columnconfigure(0, weight=1)
input_frame.columnconfigure(1, weight=1)

email_lb = tk.Label(input_frame, text="Email", font=("Inter", 10))
email_in = tk.Entry(input_frame)
email_lb.grid(column=0, row=0, sticky=tk.W+tk.E, padx=10)
email_in.grid(column=0, row=1, sticky=tk.W+tk.E, padx=10)

password_lb = tk.Label(input_frame, text="Password", font=("Inter", 10))
password_in = tk.Entry(input_frame)
password_lb.grid(column=1, row=0, sticky=tk.W+tk.E, padx=10)
password_in.grid(column=1, row=1, sticky=tk.W+tk.E, padx=10)

input_frame.pack(fill="x")

root.mainloop()
