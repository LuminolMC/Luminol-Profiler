import tkinter as tk
import ttkbootstrap as ttk
import network.ConnectionManager
from ttkbootstrap.constants import *


class MainWindow:
    def __init__(self):
        self.chunk_frame = None
        self.chunk_view = None
        self.rect = []
        self.chunk_canvas_frame = []
        self.window = tk.Tk()
        self.window.geometry('1000x500')
        self.window.columnconfigure(0, weight=1)
        self.window.title("Luminol Profiler - Unconnected")
        self.create_menu_bar()

    def connect_window(self):
        def connect():
            uri = uri_entry.get()
            network.connection.connect(uri)

        connecting_window = tk.Toplevel(self.window)
        connecting_window.title("Connect to server")
        connecting_window.geometry("350x150")
        screen_width = connecting_window.winfo_screenwidth()

        frame = ttk.Frame(connecting_window)
        uri_entry = ttk.Entry(frame, width=50)
        connect_button = ttk.Button(frame, text="Connect", command=connect)
        frame.pack(anchor=CENTER, expand=True)
        uri_entry.pack(padx=5, pady=10)
        connect_button.pack(padx=5, pady=5)

    # 顶部菜单
    def create_menu_bar(self):
        menubar = ttk.Menu(self.window)
        menubar.add_command(label="Connect", command=self.connect_window)
        self.window.config(menu=menubar)

    def create_perf_canvas(self):
        cpu_load = ttk.Canvas(self.window)

    def create_chunk_view(self):
        self.chunk_frame = ttk.Frame(self.window)
        self.chunk_canvas_frame = ttk.Frame(self.chunk_frame)
        self.chunk_view = []
        self.rect = []
        for i in range(16):
            c = []
            r = []
            for j in range(16):
                chunk_canvas = ttk.Canvas(self.chunk_canvas_frame, width=20, height=20)
                rect = chunk_canvas.create_rectangle(0, 0, 20, 20, fill="grey", outline="black")
                chunk_canvas.grid(row=i, column=j)
                c.append(chunk_canvas)
                r.append(rect)
                self.chunk_view.append(c)
                self.rect.append(r)
        self.chunk_canvas_frame.pack(padx=5)
        self.chunk_frame.pack(anchor="e")
        self.chunk_view[0][0].itemconfig(self.rect[0][0], fill="blue")

    def mainloop(self):
        self.create_menu_bar()
        self.create_perf_canvas()
        self.create_chunk_view()
        self.window.mainloop()
