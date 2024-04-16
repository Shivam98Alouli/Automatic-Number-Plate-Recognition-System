import cv2
import easyocr
import imutils
import numpy as np
from src.gui.button_switch import ButtonSwitch
from src.assets.interface import *
from src.assets.update_db import *

class ANPR(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#c9b4d9')
        self.controller = controller

        """Separators."""
        sep_y = 35
        sep_s = 50

        """Coordinates"""
        lbl_sw_x = 30
        lbl_sw_y = 130
        lbl_sl_x = 30
        lbl_sl_y = 350
        btn_sw_x = 110
        btn_sw_y = 125
        btn_y = 620
        sl_x = 30
        sl_y = 370

        """Labels."""
        # Title
        background = '#c9b4d9'
        tk_interface(self, "Automatic Number-Plate Recognition", background)
        # Options
        lbl_filter = tk.Label(self, text="Filters", font=("Arial Bold", 10), fg='blue', bg=background)
        lbl_filter.place(x=70, y=100)
        lbl_settings = tk.Label(self, text="Settings", font=("Arial Bold", 10), fg='blue', bg=background)
        lbl_settings.place(x=70, y=330)
        # Toggles
        lbl_gray = tk.Label(self, text="GrayScale", font=("Arial", 10), bg=background)
        lbl_gray.place(x=lbl_sw_x, y=lbl_sw_y)
        lbl_bfilter = tk.Label(self, text="BilatFilter", font=("Arial", 10), bg=background)
        lbl_bfilter.place(x=lbl_sw_x, y=lbl_sw_y + sep_y)
        lbl_canny = tk.Label(self, text="Canny", font=("Arial", 10), bg=background)
        lbl_canny.place(x=lbl_sw_x, y=lbl_sw_y + sep_y*2)
        lbl_mask = tk.Label(self, text="Mask", font=("Arial", 10), bg=background)
        lbl_mask.place(x=lbl_sw_x, y=lbl_sw_y + sep_y * 3)
        lbl_contour = tk.Label(self, text="Contour", font=("Arial", 10), bg=background)
        lbl_contour.place(x=lbl_sw_x, y=lbl_sw_y + sep_y * 4)
        # Sliders
        lbl_s_iteration = tk.Label(self, text="Iteration", font=("Arial Bold", 10), bg=background)
        lbl_s_iteration.place(x=lbl_sl_x, y=lbl_sl_y)
        lbl_s_sigma = tk.Label(self, text="Sigma", font=("Arial Bold", 10), bg=background)
        lbl_s_sigma.place(x=lbl_sl_x, y=lbl_sl_y + sep_s)
        lbl_s_canny_l = tk.Label(self, text="Canny Low", font=("Arial Bold", 10), bg=background)
        lbl_s_canny_l.place(x=lbl_sl_x, y=lbl_sl_y + sep_s*2)
        lbl_s_canny_h = tk.Label(self, text="Canny High", font=("Arial Bold", 10), bg=background)
        lbl_s_canny_h.place(x=lbl_sl_x, y=lbl_sl_y + sep_s * 3)
        # Number Info
        self.number = ""
        self.lbl_num = tk.Label(self, width=12, bg='white', font=('Arial', 12), text=self.number)
        self.lbl_num.place(x=440, y=621)

        """Buttons."""
        btn_menu = tk.Button(self, text='Menu', command=lambda: controller.up_frame("Menu"))
        btn_menu.place(x=757, y=btn_y)
        btn_db = tk.Button(self, text='AddData', command=lambda: open_db_np(self))
        btn_db.place(x=279, y=btn_y)
        btn_check = tk.Button(self, text='Check', command=lambda: check_db_np(self))
        btn_check.place(x=336, y=btn_y)
        btn_num = tk.Button(self, text='Number', command=lambda: num_plate(self))
        btn_num.place(x=380, y=btn_y)

        """Toggle Switches."""
        self.btn_sw_gray = ButtonSwitch(self, background)
        self.btn_sw_gray.place(x=btn_sw_x, y=btn_sw_y)
        self.btn_sw_bfilter = ButtonSwitch(self, background)
        self.btn_sw_bfilter.place(x=btn_sw_x, y=btn_sw_y + sep_y)
        self.btn_sw_canny = ButtonSwitch(self, background)
        self.btn_sw_canny.place(x=btn_sw_x, y=btn_sw_y + sep_y*2)
        self.btn_mask = ButtonSwitch(self, background)
        self.btn_mask.place(x=btn_sw_x, y=btn_sw_y + sep_y * 3)
        self.btn_contour = ButtonSwitch(self, background)
        self.btn_contour.place(x=btn_sw_x, y=btn_sw_y + sep_y * 4)

        """Sliders."""
        self.var_iteration = tk.IntVar()
        sl_iteration = tk.Scale(self, from_=1, to=21, length=130, width=4, orient='horizontal',
                                font=('Console', 10), resolution=1, variable=self.var_iteration,
                                bg=background, troughcolor='white', highlightthickness=0)
        sl_iteration.place(x=sl_x, y=sl_y)

        self.var_sigma = tk.IntVar()
        sl_kernel = tk.Scale(self, from_=1, to=31, length=130, width=4, orient='horizontal',
                             font=('Console', 10), resolution=1, variable=self.var_sigma,
                             bg=background, troughcolor='white', highlightthickness=0)
        sl_kernel.place(x=sl_x, y=sl_y + sep_s)

        self.var_canny_l = tk.IntVar()
        sl_canny_l = tk.Scale(self, from_=1, to=151, length=130, width=4, orient='horizontal',
                              font=('Console', 10), resolution=1, variable=self.var_canny_l,
                              bg=background, troughcolor='white', highlightthickness=0)
        sl_canny_l.place(x=sl_x, y=sl_y + sep_s*2)

        self.var_canny_h = tk.IntVar()
        sl_canny_h = tk.Scale(self, from_=1, to=301, length=130, width=4, orient='horizontal',
                              font=('Console', 10), resolution=1, variable=self.var_canny_h,
                              bg=background, troughcolor='white', highlightthickness=0)
        sl_canny_h.place(x=sl_x, y=sl_y + sep_s * 3)

    def update_img(self, frame):
        self.orig_img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        cv2_img = self.orig_img

        if self.btn_sw_gray.is_off == False:
            self.gray_img = cv2.cvtColor(cv2_img, cv2.COLOR_RGB2GRAY)
            cv2_img = self.gray_img

        if self.btn_sw_bfilter.is_off == False:
            cv2_img = cv2.bilateralFilter(cv2_img, self.var_iteration.get(), self.var_sigma.get(), self.var_sigma.get())

        if self.btn_sw_canny.is_off == False:
            cv2_img = cv2.Canny(cv2_img, self.var_canny_l.get(), self.var_canny_h.get(), 2)

        if self.btn_mask.is_off == False:
            keypoints = cv2.findContours(cv2_img.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            contours = imutils.grab_contours(keypoints)
            contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

            for contour in contours:
                self.approx = cv2.approxPolyDP(contour, 10, True)
                if len(self.approx) == 4:
                    self.location = self.approx
                    break

            self.mask = np.zeros(self.gray_img.shape, np.uint8)
            cv2_img = cv2.drawContours(self.mask, [self.location], 0, 255, -1)
            cv2_img = cv2.bitwise_and(self.orig_img, self.orig_img, mask=self.mask)

        if self.btn_contour.is_off == False:
            """Cropping Image"""
            try:
                (x, y) = np.where(self.mask == 255)
                (x1, y1) = (np.min(x), np.min(y))
                (x2, y2) = (np.max(x), np.max(y))
                cropped_img = self.gray_img[x1:x2+1, y1:y2+1]
                cv2_img = cv2.rectangle(self.orig_img, tuple(self.approx[0][0]), tuple(self.approx[2][0]), (0, 255, 0), 2)
            except IndexError:
                raise messagebox.showerror("IndexError", "Can't be found the number plate contour")

            """Read Text from Image"""
            reader = easyocr.Reader(['en'], gpu=False)
            results = reader.readtext(cropped_img)
            self.text = ""
            for i in range(len(results)):
                self.text += results[i][-2]
                self.text = self.text.replace(".", "")
                self.number = self.text.replace(" ", "")

            cv2.putText(self.orig_img, self.number, (10, 20), 1, 2, (255, 0, 0), 2)

        img = Image.fromarray(cv2_img)
        img = img.resize((599, 557), Image.ANTIALIAS)
        img_tk = ImageTk.PhotoImage(image=img)
        self.lbl_img = tk.Label(self, image=img_tk)
        self.lbl_img.imgtk = img_tk
        self.lbl_img.place(x=200, y=50)

