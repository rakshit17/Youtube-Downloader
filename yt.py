from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=UT58ETAj3cg")
down =yt.streams.get_by_itag(22)

down.download("Storage Path")
