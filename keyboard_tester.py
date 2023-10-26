import tkinter as tk

import customtkinter as ctk
from number_pad_keys import keyboard_keys

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.width = 1455
        self.height = 450
        self.matrix = []
        self.label = None
        self.run()

    def run(self):
        self.resizable(False, False)
        self.title("Keyboard Tester")

        self.frame = ctk.CTkFrame(self, width=self.width, height=self.height)
        self.frame.pack()

        main_menu = tk.Menu(self)
        self.config(menu=main_menu)

        program_menu = tk.Menu(main_menu)
        main_menu.add_cascade(label="Program", menu=program_menu)
        program_menu.add_command(label="Restart", command=lambda: self.restart())
        program_menu.add_command(label="Exit", command=lambda: self.destroy())

        self.label = ctk.CTkLabel(self, text="Press any button", font=('Bold', 30))
        self.label.place(x=700, y=410, anchor=tk.CENTER)

        for i in keyboard_keys:
            btn = self.create_btn(width=i['width'], height=i['height'], text=i['name'], font=("Bold", 12))
            btn.place(x=i['pos_x'], y=i['pos_y'])
            self.matrix += [btn]

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (self.width / 2)
        y = (screen_height / 2) - (self.height / 2)
        self.geometry(f"{self.width}x{self.height}+{int(x)}+{int(y)}")

        self.bind('<Key>', lambda event: self.check_key(event))

        self.mainloop()

    def restart(self):
        self.label.destroy()
        for key in keyboard_keys:
            self.matrix[keyboard_keys.index(key)].configure(fg_color="#3B8ED0")
        self.run()

    def check_key(self, event):
        keysym = event.keysym.lower()
        self.label.configure(text=f"{keysym} {event.keycode}")
        for key in keyboard_keys:
            if keysym in key['key']:
                self.matrix[keyboard_keys.index(key)].configure(fg_color='red')
                break

    def create_btn(self, **kwargs):
        return ctk.CTkButton(self.frame, hover=False, **kwargs)

