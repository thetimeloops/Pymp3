import my_functions as my

def main():
    youtube_link =input("Paste youtube url here(no playlist): ")
    print("")
    print("Searching for Youtube Video")
    print("")
#    if youtube_link.find("playlist?")>-1:
#        print("work in progress...")
#    elif youtube_link.find("watch?")>-1:
    try:
        vid = youtube_link[(youtube_link.find("watch?v=")+8):len(youtube_link)]
        title_response = my.get_response(f"https://mp3download.center/download/{vid}").find("div",{"class":"col-lg-12"}).h1.text
        start = title_response.find("Download")+9
        end = title_response.find("MP3")-1
        title = title_response[start:end]
        quality="320"
        print("")
        print(f"Downloading {title}")
        my.downloader(vid,quality,title)
    except:
        print("wrong link")
