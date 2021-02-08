# MKV to MP4
This is a tool created for a plex server to convert all the mkv, uncompressed bad file formats for streaming,
to mp4 for better streaming performance for direct streaming.

## What does it do
Simple, looks through all the sub direcotrs in the director selected looking for mkv to then convert it to mp4, does it by changing container
of the data.


# TODO
* Make an automatic mode to search on a schedule
* Show a percentage done of current conversion (time completed/total time)
* Hide the terminal when running(build python)
    * Make it so it forces run as admin so it supports deleting of the file after
* Improve the compression of the mp4 file at the end
