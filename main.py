import tkinter as tk
from piexif import load, ImageIFD, dump
from PIL import Image
from os import listdir
from pathlib import Path

def master_check():
    try:
        listdir("resources/close")
    except FileNotFoundError:
        return False
    else:
        try:
            img = Image.open("resources/close/close.jpeg")
        except FileNotFoundError:
            return False
        else:
            exif_data = img.info.get("exif")
            if exif_data:
                exif_dict = load(exif_data)
                if exif_dict["0th"][ImageIFD.Artist] == "MASTER":
                    if len(exif_dict["0th"][ImageIFD.ImageDescription]) != 0:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False



# root_img_path = "resources/root/logo.jpeg"
#
# root_img = Image.open(root_img_path)
#
# def master():
#     try:
#         master_img_path = "resources/root/close.jpeg"
#         master_img = Image.open(master_img_path)
#     except FileNotFoundError:
#
#     def master_check():
#
#
#
#         exif_dict = load(master_img.info.get("exif"))
#         exif_dict["0th"][ImageIFD.ImageDescription] = "var"
#         exif_dict["0th"][ImageIFD.DateTime] = "var"
#         # Convert to EXIF bytes
#         exif_bytes = dump(exif_dict)
#         # Save with new metadata
#         root_img.save(f"resources/close/close.jpeg", exif=exif_bytes)
#         return True
#     else:
#         return False
#
# def add(root, path, var):
#     # path = "resources/icons"
#     resource_len = 0
#     try:
#         resource_len = len(listdir(path))
#     except FileNotFoundError:
#         Path(path).mkdir(parents=True, exist_ok=True)
#     finally:
#         exif_dict = load(root.info.get("exif"))
#         exif_dict["0th"][ImageIFD.ImageDescription] = "var"
#         exif_dict["0th"][ImageIFD.DateTime] = "var"
#         # Convert to EXIF bytes
#         exif_bytes = dump(exif_dict)
#         # Save with new metadata
#         root.save(f"{path}/{resource_len + 1}.jpeg", exif=exif_bytes)


root = tk.Tk()
root.title("Password Manager")
root.geometry("650x450")


label = tk.Label(root, text="Welcome", font=("Inter", 20, "bold"))
label.pack(padx=10, pady=10)

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
