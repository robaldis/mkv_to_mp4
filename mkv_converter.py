import os
import ffmpeg

def mkv_to_mp4(mkv_file):
    print(mkv_file)
    name, ext = os.path.splitext(mkv_file)
    print(name, ext)
    out_name = name + ".mp4"
    ffmpeg.input(mkv_file).output(out_name).run()
    print(f"Finished converting {mkv_file}")

def search_sub_dir(directory):
    for root, dirs, files in os.walk(directory, topdown=False):
        print(root)
        for name in files:
            print(name[-4:])
            if name[-4:] == ".mkv":
                print(f"Starting conversion on {name}")
                mkv_to_mp4(os.path.join(root, name))


if __name__ == "__main__":
    print("starting")
    search_sub_dir(os.path.join(os.getcwd(), "movies"))
