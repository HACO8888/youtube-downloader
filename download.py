from pytube import YouTube
from pytube.cli import on_progress
print('請輸入要下載的影片')
urll = input()
print('請輸入要存入的路徑')
pathh = input()
def yt_dl(url):
        try:
            yt = YouTube(url, on_progress_callback=on_progress)
            print(f'影片名稱:{yt.title}')
            print(f'影片縮圖:{yt.thumbnail_url}')
            print(f'檔案位置:{pathh}\{yt.title}.mp4')
            yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution().download(pathh)

    
	    
        except EOFError as err:
            print(err)

        else:
            print("\n========")
            print("\n下載完成")
            print("\n========")


if __name__ == '__main__':
	yt_dl(urll)