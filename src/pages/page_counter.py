from src.gui.button_switch import ButtonSwitch
from src.assets.interface import *

class Counter(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#83CDEA')
        self.controller = controller

        """Separators."""
        sep = 35
        sep_s = 50

        """Coordinates"""
        lbl_sw_x = 30
        lbl_sw_y = 130
        lbl_sl_x = 30
        lbl_sl_y = 300
        btn_sw_x = 110
        btn_sw_y = 125
        sl_x = 30
        sl_y = 320

        """Background color."""
        background = '#83CDEA'

        """Labels."""
        # Title
        tk_interface(self, "Counter", background)
        # Options
        lbl_filter = tk.Label(self, text="Filters", font=("Arial Bold", 10), fg='blue', bg=background)
        lbl_filter.place(x=70, y=100)
        lbl_settings = tk.Label(self, text="Settings", font=("Arial Bold", 10), fg='blue', bg=background)
        lbl_settings.place(x=70, y=280)
        # Number Info
        self.number = 0
        self.cnt = []
        self.lbl_num = tk.Label(self, width=8, bg='white', font=('Arial', 12), text=int(self.number))
        self.lbl_num.place(x=480, y=621)

        # Toggles
        lbl_gray = tk.Label(self, text="GrayScale", font=("Arial", 10), bg=background)
        lbl_gray.place(x=lbl_sw_x, y=lbl_sw_y)
        lbl_canny = tk.Label(self, text="Canny", font=("Arial", 10), bg=background)
        lbl_canny.place(x=lbl_sw_x, y=lbl_sw_y + sep)
        lbl_dilate = tk.Label(self, text="Dilate", font=("Arial", 10), bg=background)
        lbl_dilate.place(x=lbl_sw_x, y=lbl_sw_y + sep * 2)
        lbl_contour = tk.Label(self, text="Contour", font=("Arial", 10), bg=background)
        lbl_contour.place(x=lbl_sw_x, y=lbl_sw_y + sep * 3)

        # Sliders
        lbl_s_blur = tk.Label(self, text="GaussianBlur", font=("Arial Bold", 10), bg=background)
        lbl_s_blur.place(x=lbl_sl_x, y=lbl_sl_y)
        lbl_s_canny_l = tk.Label(self, text="Canny Low", font=("Arial Bold", 10), bg=background)
        lbl_s_canny_l.place(x=lbl_sl_x, y=lbl_sl_y + sep_s)
        lbl_s_canny_h = tk.Label(self, text="Canny High", font=("Arial Bold", 10), bg=background)
        lbl_s_canny_h.place(x=lbl_sl_x, y=lbl_sl_y + sep_s * 2)
        lbl_s_kernel = tk.Label(self, text="Kernel", font=("Arial Bold", 10), bg=background)
        lbl_s_kernel.place(x=lbl_sl_x, y=lbl_sl_y + sep_s * 3)
        lbl_s_iteration = tk.Label(self, text="Iteration", font=("Arial Bold", 10), bg=background)
        lbl_s_iteration.place(x=lbl_sl_x, y=lbl_sl_y + sep_s * 4)

        """Buttons."""
        btn_menu = tk.Button(self, text='Menu', command=lambda: controller.up_frame("Menu"))
        btn_menu.place(x=757, y=620)
        btn_objects = tk.Button(self, text='Objects', command=lambda: num_of_it(self))
        btn_objects.place(x=425, y=620)

        """Toggle Switches."""
        self.btn_sw_gray = ButtonSwitch(self, background)
        self.btn_sw_gray.place(x=btn_sw_x, y=btn_sw_y)
        self.btn_sw_canny = ButtonSwitch(self, background)
        self.btn_sw_canny.place(x=btn_sw_x, y=btn_sw_y + sep)
        self.btn_sw_dilate = ButtonSwitch(self, background)
        self.btn_sw_dilate.place(x=btn_sw_x, y=btn_sw_y + sep * 2)
        self.btn_sw_contour = ButtonSwitch(self, background)
        self.btn_sw_contour.place(x=btn_sw_x, y=btn_sw_y + sep * 3)

        """Sliders."""
        self.var_blur = tk.IntVar()
        sl_blur = tk.Scale(self, from_=1, to=121, length=130, width=4, orient='horizontal',
                           font=('Console', 10), resolution=2, variable=self.var_blur,
                           bg=background, troughcolor='white', highlightthickness=0)
        sl_blur.place(x=sl_x, y=sl_y)

        self.var_canny_l = tk.IntVar()
        sl_canny_l = tk.Scale(self, from_=1, to=151, length=130, width=4, orient='horizontal',
                              font=('Console', 10), resolution=1, variable=self.var_canny_l,
                              bg=background, troughcolor='white', highlightthickness=0)
        sl_canny_l.place(x=sl_x, y=sl_y + sep_s)

        self.var_canny_h = tk.IntVar()
        sl_canny_h = tk.Scale(self, from_=1, to=301, length=130, width=4, orient='horizontal',
                              font=('Console', 10), resolution=1, variable=self.var_canny_h,
                              bg=background, troughcolor='white', highlightthickness=0)
        sl_canny_h.place(x=sl_x, y=sl_y + sep_s * 2)

        self.var_kernel = tk.IntVar()
        sl_kernel = tk.Scale(self, from_=1, to=11, length=130, width=4, orient='horizontal',
                             font=('Console', 10), resolution=1, variable=self.var_kernel,
                             bg=background, troughcolor='white', highlightthickness=0)
        sl_kernel.place(x=sl_x, y=sl_y + sep_s * 3)

        self.var_iteration = tk.IntVar()
        sl_iteration = tk.Scale(self, from_=1, to=21, length=130, width=4, orient='horizontal',
                                font=('Console', 10), resolution=1, variable=self.var_iteration,
                                bg=background, troughcolor='white', highlightthickness=0)
        sl_iteration.place(x=sl_x, y=sl_y + sep_s * 4)

    def update_img(self, frame):
        cv2_img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        cv2_img = cv2.GaussianBlur(cv2_img, (self.var_blur.get(), self.var_blur.get()), 0)
        if self.btn_sw_gray.is_off == False:
            cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_RGB2GRAY)
        if self.btn_sw_canny.is_off == False:
            cv2_img = cv2.Canny(cv2_img, self.var_canny_l.get(), self.var_canny_h.get(), 2)
        if self.btn_sw_dilate.is_off == False:
            cv2_img = cv2.dilate(cv2_img, (self.var_kernel.get(), self.var_kernel.get()),
                                 iterations=self.var_iteration.get())
        if self.btn_sw_contour.is_off == False:
            (self.cnt, hierarchy) = cv2.findContours(cv2_img.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            cv2_img = cv2.drawContours(rgb, self.cnt, -1, (0, 255, 0), 2)
        img = Image.fromarray(cv2_img)
        img = img.resize((599, 557), Image.ANTIALIAS)
        img_tk = ImageTk.PhotoImage(image=img)
        self.lbl_img = tk.Label(self, image=img_tk)
        self.lbl_img.imgtk = img_tk
        self.lbl_img.place(x=200, y=50)