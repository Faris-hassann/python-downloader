from pytube import YouTube

link = input("enter the url link here: ")

video = YouTube(link)

print(f"the video title is: \n{video.title}")
print ("===================================================")

print (f"the video view are: \n{video.views}")
print ("===================================================")

print (f"the video duration are: \n{video.length}")
print ("===================================================")

def finish():
    print("download done! check it out")

video.streams.get_highest_resolution().download(output_path="/Downloads/")

video.register_on_complete_callback(finish())