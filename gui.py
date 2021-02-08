import tkinter.filedialog
import tkinter as tk
import mkv_converter as converter


# tk and tkinter are different, how?

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.wait_time = 3600000
        self.master = master
        self.pack()
        self.create_widgets()
        self.conv = converter.Converter()
        self.after(self.wait_time, self.loop)
    
    def loop(self):
        self.conv.auto_convertion()
        self.after(self.wait_time, self.loop)

    def create_widgets(self):
        # Place to create widgets

        self.dire = tk.Label(self)
        self.dire.pack()

        # Creating a widget like this can be done as a one liner like this
        self.hi_there = tk.Button(self, text="Select path", command=self.select_file)
        self.hi_there.pack(side="top")

        self.convert = tk.Button(self, text="Convert MKV to MP4", command=self.convert)
        self.convert.pack()

        date = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]

        self.var_start = tk.StringVar()
        self.var_start.set(0)
        self.schedule_start = tk.OptionMenu(self, self.var_start, *date, command=self.set_schedule_start)
        self.schedule_start.pack()
        self.var_end = tk.StringVar()
        self.var_end.set(0)
        self.schedule_end = tk.OptionMenu(self, self.var_end, *date, command=self.set_schedule_end)
        self.schedule_end.pack()

        self.auto_mode = tk.Button(self, text="Auto Mode",relief="raised", command=self.toggle_auto)
        self.auto_mode.pack()

        self.message = tk.Label(self)
        self.message.pack()




        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")



    def select_file(self):
        dire = tk.filedialog.askdirectory(initialdir=".", title="")
        self.dire["text"] = dire
        self.conv.set_dir(dire)

    def convert(self):
        target = self.dire["text"]
        self.conv.search_sub_dir()
        self.message["text"] = "Done!"


    def set_schedule_start(self, *args):
        self.conv.set_schedule_start(self.var_start.get())

    def set_schedule_end(self, *args):
        self.conv.set_schedule_end(self.var_end.get())

    def toggle_auto(self):
        if self.auto_mode.config('relief')[-1] == 'sunken':
            self.auto_mode.config(relief="raised")
            self.conv.set_auto(False)
        else:
            self.auto_mode.config(relief="sunken")
            self.conv.set_auto(True)
            self.conv.auto_convertion()
        

        
root = tk.Tk()
app = Application(master=root)
app.mainloop()
