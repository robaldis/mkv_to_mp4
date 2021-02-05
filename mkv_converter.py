import os
import ffmpeg

def mkv_to_mp4(mkv_file):
    name, ext = os.path.splittext(mkv_file)
    out_name = name + ".mp4"
    ffmpeg.input(mkv_file).output(out_name).run()
    print(f"Finished converting {mkv_file}")


