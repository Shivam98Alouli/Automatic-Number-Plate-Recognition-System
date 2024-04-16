from tkinter import filedialog
from PIL import ImageTk, Image
import cv2
from src.assets.update_db import *

"""Open functions."""
def open_img(self):
    delete_img(self)
    try:
        self.file_img = tk.filedialog.askopenfilename(filetypes=[
            ('JPG files', '*.jpg'),
            ('PNG files', '*.png')])
        if len(self.file_img) > 0:
            self.lbl_f_path.configure(text=self.file_img)
            img = cv2.imread(self.file_img)
            self.update_img(img)
    except cv2.error:
        return messagebox.showerror("Error:215", "Black and white images are not supported. Please select a color image!")

def open_video(self):
    delete_img(self)
    self.v_path = tk.filedialog.askopenfilename(filetypes=[
        ('AVI files', '*.avi'),
        ('MP4 files', '*.mp4')])
    if len(self.v_path) > 0:
        self.lbl_f_path.configure(text=self.v_path)
        self.cap = cv2.VideoCapture(self.v_path)
        update_video(self)

def open_cam(self):
    delete_img(self)
    self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    self.lbl_f_path.configure(text='WebCam')
    update_video(self)

"""Update functions."""

def update_video(self):
    if self.cap is not None:
        ret, frame = self.cap.read()
        if ret == True:
            self.update_img(frame)
            self.lbl_img.after(10, lambda: update_video(self))

"""Render functions."""

def refresh_img(self):
    delete_img(self)
    self.lbl_f_path.configure(text=self.file_img)
    img = cv2.imread(self.file_img)
    self.update_img(img)

def delete_img(self):
    if self.cap is not None:
        self.cap.release()
        self.cap = None
    self.lbl_f_path.configure(text="Any file is not opened")
    self.lbl_img.imgtk = ""

def num_of_it(self):
    self.number = len(self.cnt)
    self.lbl_num.destroy()
    self.lbl_num = tk.Label(self, width=8, bg='white', font=('Arial', 12), text=int(self.number))
    self.lbl_num.place(x=480, y=621)

def num_plate(self):
    self.lbl_num.destroy()
    self.number = self.text.replace(" ", "")
    self.lbl_num = tk.Label(self, width=12, bg='white', font=('Arial', 12), text=self.number)
    self.lbl_num.place(x=440, y=621)

def open_db_np(self):
    self.db = UpdateDB()

def check_db_np(self):
    db = PlateNum_DB('../src/resources/num_plate_db/num_plates.db')
    plate_info = db.read_one(self.number)
    messagebox.showinfo("Number Plate", plate_info)

