import os
import ffmpeg
import time

class Converter ():
    def __init__(self):
        self.AUTO_MODE = False
        self.directory = ""
        self.schedule_start = "0"
        self.schedule_end = "0"

    def auto_convertion(self):
        # mkv_to_mp4(self.convert_queue[0])

        print(self.AUTO_MODE, self.check_in_schedule())
        if (self.AUTO_MODE and self.check_in_schedule()):
            self.search_sub_dir()

        
        

    def mkv_to_mp4(self, mkv_file):
        name, ext = os.path.splitext(mkv_file)
        out_name = name + ".mp4"
        ffmpeg.input(mkv_file).output(out_name).compile(overwrite_output=False)
        print(f"Finished converting {mkv_file}")
        # os.remove(mkv_file)

    def search_sub_dir(self):
        print("searching")
        for root, dirs, files in os.walk(self.directory, topdown=False):
            print(dirs)
            for name in files:
                print(name)
                if name[-4:] == ".mkv":
                    print(f"Starting conversion on {name}")
                    self.mkv_to_mp4(os.path.join(root, name))

    def check_in_schedule(self) -> bool:
        # check if the current time is between the scheduled time
        # get the current hour in 24hr format
        current_time = time.strftime("%H")

        print(current_time)
        if (current_time >= self.schedule_start and current_time <= self.schedule_end):
            # inside schedule time
            return True
        return False

    def set_schedule_start(self, time):
        print("[set_schedule_start] "  + time)
        self.schedule_start = time

    def set_schedule_end(self, time):
        print("[set_schedule_end] " + time)
        self.schedule_end = time

    def set_auto(self, val):
        self.AUTO_MODE = val
        print(self.AUTO_MODE)

    def set_dir(self, val):
        self.directory = val


if __name__ == "__main__":
    search_sub_dir(os.path.join(os.getcwd(), "movies"))
