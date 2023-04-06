import tkinter as tk
import os
from tkinter import messagebox


class AppStart:

    # _____________GUI_____________
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("AoEGroup")
        self.window.config(bg="black", pady=50, padx=50)
        self.window.rowconfigure(0, weight=1)
        self.window.columnconfigure(0, weight=1)
        self.MAIN_IMAGE = tk.PhotoImage(file="./bot/screens/aoe.png")
        self.canvas = tk.Canvas(width=200, height=133, highlightthickness=0)
        self.canvas.create_image(100, 66, image=self.MAIN_IMAGE)
        self.canvas.grid(column=0, row=0)
        self.server_canvas = tk.Canvas(width=200, height=133, highlightthickness=0, bg="black")

        self.frame_1 = tk.Frame()
        self.frame_2 = tk.Frame()
        self.frame_3 = tk.Frame()
        self.frame_4 = tk.Frame()
        self.frame_5 = tk.Frame()
        self.frame_6 = tk.Frame()

        self.frame_1_call()

        self.window.mainloop()

    #trade bot, buy bot
    def frame_1_call(self):
        bot_button_f1 = tk.Button(self.frame_1,
                                  text="Trade Bot",
                                  font=("Aerial", 15, "bold"),
                                  width=13,
                                  command=lambda: self.show_frame(self.frame_2_call(), current_frame=self.frame_1))
        bot_button_f1.grid(row=1, column=0)
        bot_button2_f1 = tk.Button(self.frame_1, text="Buy Bot", font=("Aerial", 15, "bold"), width=13)
        bot_button2_f1.grid(row=2, column=0)
        self.frame_1.grid()

    # choose server, new server, back
    def frame_2_call(self):
        bot_button_f2 = tk.Button(self.frame_2,
                                  text="Choose Server",
                                  font=("Aerial", 15, "bold"),
                                  width=13,
                                  command=lambda: self.show_frame(self.frame_4_call(), current_frame=self.frame_2))
        bot_button_f2.grid(row=1, column=0)
        bot_button2_f2 = tk.Button(self.frame_2,
                                   text="New Server",
                                   font=("Aerial", 15, "bold"),
                                   width=13,
                                   command=lambda: self.show_frame(self.frame_3_call(), current_frame=self.frame_2))
        bot_button2_f2.grid(row=2, column=0)
        back_btn_f2 = tk.Button(self.frame_2,
                                text="Back",
                                font=("Aerial", 15, "bold"),
                                width=13,
                                command=lambda: self.show_frame(self.frame_1_call(), current_frame=self.frame_2))
        back_btn_f2.grid(row=3, column=0)
        self.frame_2.grid()

    # entry, create, back
    def frame_3_call(self):
        entry = tk.Entry(self.frame_3,
                         font=("Aerial", 15, "bold"),
                         width=13)
        entry.grid(row=1, column=0)
        entry.insert(0, "Server Name")
        create_btn = tk.Button(self.frame_3,
                                text="Create",
                                font=("Aerial", 15, "bold"),
                                width=13,
                                command=lambda: self.show_frame(
                                    self.new_server_create(entry.get()), current_frame=self.frame_3))
        create_btn.grid(row=2, column=0)
        back_btn = tk.Button(self.frame_3,
                                text="Back",
                                font=("Aerial", 15, "bold"),
                                width=13,
                                command=lambda: self.show_frame(self.frame_2_call(), current_frame=self.frame_3))
        back_btn.grid(row=3, column=0)
        self.frame_3.grid()

    def frame_4_call(self):
        files = [file for file in os.listdir("./servers")]
        self.server_canvas.create_text(100, 30,
                                       text=f"{files[0]}",
                                       tags=f"text_{files[0]}",
                                       fill="white",
                                       font=("Aerial", 15, "bold"))
        self.server_canvas.grid()
        self.canvas.tag_bind(f"text_{files[0]}", "<Button-1>", func=self.server_options)
        print(files)
        print(f"text_{files[0]}")
        # y = 0
        # for file in files:
        #     y += 30
        #     self.server_canvas.create_text(100, y,
        #                                    text=f"{file}",
        #                                    tags=f"text_{file}",
        #                                    fill="white",
        #                                    font=("Aerial", 15, "bold"))
        #     self.server_canvas.grid()
        #     self.canvas.tag_bind(f"text_{file}", "<Button-1>", func=self.server_options)

    def show_frame(self, *args, current_frame):
        current_frame.grid_forget()

    def new_server_create(self, server):
        if not os.path.exists(f"./servers/{server}"):
            os.mkdir(f"./servers/{server}")
            messagebox.showinfo(title="Successful", message=f"{server} was created!")
        else:
            messagebox.showerror(title="Alo", message=f"{server} is already existed!")
        self.show_frame(self.frame_1_call(), current_frame=self.frame_3)

    def server_options(self):
        print("here")


#TODO 1: Change structure so choosing server will be first option and only then there will be variants what to do with them