from pytube import YouTube
from plyer import notification #for getting notification on your PC


def download_video():
    #ask for the link from user
    link = input("Enter the link of YouTube video you want to download:  ")
    yt = YouTube(link)

    #Getting the highest resolution possible
    ys = yt.streams.get_highest_resolution()

    #Starting download
    print("Downloading...")

    notification.notify(
        title = "Downloading ",
        message = yt.title,
        app_icon = "Dakirby309-Simply-Styled-YouTube.ico",
        timeout = 10
    )
    ys.download()

def main():
    download_video()
if __name__ == '__main__':
    main()