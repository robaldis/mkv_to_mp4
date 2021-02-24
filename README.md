# MKV to MP4
This is a tool created for a plex server to convert all the mkv, uncompressed bad file formats for streaming,
to mp4 for better streaming performance for direct streaming.

## What does it do
Simple, looks through all the sub direcotrs in the director selected looking for mkv to then convert it to mp4, does it by changing container
of the data.


# TODO
* Show a percentage done of current conversion (time completed/total time)
* Hide the terminal when running(build python)
    * Make it so it forces run as admin so it supports deleting of the file after
* Setup a different media type (tv shows, movies, 4k content) this will be defined with a 
  folder that contains all this content and have configureation to define what bitrate 
  to make that content when converting
