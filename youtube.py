import yt_dlp
import os

# Specify the YouTube video URL
video_url = 'https://www.youtube.com/watch?v=rHi-8gf_UOI'

# Create an instance of yt-dlp with the desired options
ydl_opts = {
    'format': 'bestvideo+bestaudio/best',  # Download the best quality video and audio
     # 'outtmpl': r'D:\videos\stories\originalStoryVideos\%(title)s.%(ext)s',  # Output file template
    'outtmpl': r'C:\Users\black2\Videos\MEmu Video\%(title)s.%(ext)s',
    'noplaylist': True,  # Ensure only a single video is downloaded
}

# Download the video and extract video information
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(video_url, download=False)
    ydl.download([video_url])

#
#
# import yt_dlp
#
# # Specify the YouTube playlist URL
# playlist_url = 'https://www.youtube.com/watch?v=1IP8rwuDX4Y&list=PL8LwzmTmvN4x8w6oFo5u9R8fUsBBl8Af6&index=1'
#
# # Create an instance of yt-dlp
# ydl_opts = {
#     'format': 'bestvideo+bestaudio/best',  # Download the best quality video and audio
#     'outtmpl': r'D:\videos\stories\BGVideos2\BGsatisfyingVideos\%(title)s.%(ext)s',  # Output file template
#     # 'noplaylist': False,  # Download all videos in the playlist
#     'playlistend': 10,  # Download only the first 5 videos in the playlist
# }
#
# # Download all videos in the playlist
# with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#     ydl.download([playlist_url])
#
