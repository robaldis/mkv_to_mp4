import tkinter.filedialog
import tkinter as tk
import mkv_converter as converter


# tk and tkinter are different, how?

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Place to create widgets

        self.dire = tk.Text(self)
        self.dire = tk.Label(self)
        self.dire.pack()

        # Creating a widget like this can be done as a one liner like this
        self.hi_there = tk.Button(self, text="Select path", command=self.select_file)
        self.hi_there.pack(side="top")

        self.convert = tk.Button(self, text="Convert MKV to MP4", command=self.convert)
        self.convert.pack()

        self.message = tk.Label(self)
        self.message.pack()

        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")


    def say_hi(self):
        print("hi there")

    def select_file(self):
        dire = tk.filedialog.askdirectory(initialdir=".", title="")
        self.dire["text"] = dire

    def convert(self):
        target = self.dire["text"]
        converter.search_sub_dir(target)
        self.message["text"] = "Done!"


        

        
root = tk.Tk()
root.protocol("WM_DELETE_WINDOW", root.inconify)
app = Application(master=root)
app.mainloop()
