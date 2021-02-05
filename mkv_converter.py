import os
import ffmpeg

def mkv_to_mp4(mkv_file):
    name, ext = os.path.splittext(mkv_file)
    out_name = name + ".mp4"
    ffmpeg.input(mkv_file).output(out_name).run()
    print(f"Finished converting {mkv_file}")

def search_sub_dir(directory);
    for root, dirs, files in os.walk(directory, topdown=False):
        for name in files:
            if name[:4:-1] == ".mkv":
                print(f"Starting conversion on {name}")
                mkv_to_mp4(name)


