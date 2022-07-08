import pytube

url = input("Enter the URL of the video: ")
path="E:/youtube/"

pytube.YouTube(url).streams.get_highest_resolution().download(path) #Download the video high quality

print("\nVideo downloaded successfully!")

