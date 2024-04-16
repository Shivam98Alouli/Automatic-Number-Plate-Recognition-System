import tkinter as tk

class Menu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#83BBE5')
        self.controller = controller

        """Title."""
        lbl_ttl = tk.Label(self, text="Computer Vision Laboratory", font=("Arial Bold", 30), bg='#83BBE5', fg='white')
        lbl_ttl.pack(side='top')

        """Buttons."""
        sep = 30
        btn_counter = tk.Button(self, text="Counter", width=10, command=lambda: controller.up_frame('Counter'))
        btn_counter.place(x=210, y=60)
        btn_anpr = tk.Button(self, text="ANPR", width=10, command=lambda: controller.up_frame('ANPR'))
        btn_anpr.place(x=210, y=60 + sep)

        btn_quit = tk.Button(text='Quit', command=quit)
        btn_quit.place(x=800, y=620)