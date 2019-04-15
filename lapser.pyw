import tkinter as tk
from tkinter import ttk
import ffmpeg
from idlelib.tooltip import Hovertip

class Window(tk.Tk):
    def __init__(self):
        super(Window, self).__init__()
        self.title("Lapser")
        try:
            self.iconbitmap("icon.ico")
        except Exception:
            pass
        self.columnconfigure(1, weight=1)

        # Main Widgets
        ttk.Label(self, text="Input Files:").grid(row=0, column=0, sticky="e")
        self.input_file = ttk.Entry(self)
        self.input_file.grid(row=0, column=1, sticky="we", padx=6, pady=2)
        Hovertip(self.input_file, "Example: /path/to/input/%04d.png")

        ttk.Label(self, text="Output File:").grid(row=1, column=0, sticky="e")
        self.output_file = ttk.Entry(self)
        self.output_file.grid(row=1, column=1, sticky="we", padx=6, pady=2)
        Hovertip(self.output_file, "Example: /path/to/output/output.mp4")

        ttk.Label(self, text="Image Framerate:").grid(row=3, column=0, sticky="e")
        self.input_framerate = ttk.Entry(self)
        self.input_framerate.grid(row=3, column=1, sticky="we", padx=6, pady=2)
        Hovertip(self.input_framerate, "Input images displayed per second")

        ttk.Label(self, text="Output File Framerate:").grid(row=4, column=0, sticky="e")
        self.output_framerate = ttk.Entry(self)
        self.output_framerate.grid(row=4, column=1, sticky="we", padx=6, pady=2)
        Hovertip(self.output_framerate, "Framerate of the output file, typically 30 or 60 if generating a video")

        run = ttk.Button(self, text="Generate Timelapse", command=self.run)
        run.grid(row=6, column=0, columnspan=2, pady=6)

    def run(self):
        stream = ffmpeg.input(self.input_file.get(), r=int(self.input_framerate.get()))
        stream = ffmpeg.filter_(stream, 'format', 'yuv420p')
        stream = ffmpeg.output(stream, self.output_file.get(), r=int(self.output_framerate.get()))
        ffmpeg.run(stream)

window = Window()
window.mainloop()
