from src.assets.commands import *
import tkinter as tk

def tk_interface(self, title, background):
    """Capture."""
    self.cap = None

    """Labels."""
    # Title
    lbl_ttl = tk.Label(self, text=title, font=("Arial Bold", 30), bg=background, fg='white')
    lbl_ttl.pack(side='top')

    # Image
    self.lbl_img = tk.Label(self, bg='#F0F0F0', width=85, height=37)
    self.lbl_img.place(x=200, y=50)
    # File Path Info
    self.lbl_f_path = tk.Label(self, text="Any file is not opened", font=("Arial", 10), bg=background)
    self.lbl_f_path.place(x=430, y=645)

    """Buttons."""
    btn_img = tk.Button(self, text='Image', command=lambda: open_img(self))
    btn_img.place(x=30, y=50)
    btn_video = tk.Button(self, text='Video', command=lambda: open_video(self))
    btn_video.place(x=74, y=50)
    btn_cam = tk.Button(self, text='Camera', command=lambda: open_cam(self))
    btn_cam.place(x=115, y=50)
    btn_ref = tk.Button(self, text='Refresh', command=lambda: refresh_img(self))
    btn_ref.place(x=30, y=620)
    btn_del = tk.Button(self, text='Delete', command=lambda: delete_img(self))
    btn_del.place(x=80, y=620)






