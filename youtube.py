import yt_dlp
import os

# Specify the YouTube video URL
video_url = 'https://www.youtube.com/watch?v=zZ7AimPACzc'

# Create an instance of yt-dlp with the desired options
ydl_opts = {
    'format': 'bestvideo+bestaudio/best',  # Download the best quality video and audio
     # 'outtmpl': r'D:\videos\stories\originalStoryVideos\%(title)s.%(ext)s',  # Output file template
    'outtmpl': r'D:\videos\stories\BGSubwayVideos/%(title)s.%(ext)s',
    'noplaylist': True,  # Ensure only a single video is downloaded
}

# Download the video and extract video information
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(video_url, download=False)
    ydl.download([video_url])



# import yt_dlp
#
# # Specify the YouTube playlist URL
# playlist_url = 'https://www.youtube.com/watch?v=W6NPritQ5ko&list=PLqKYiplTJW4micw40v8ZdYOZBhMYGa5ro&index=1'
#
# # Create an instance of yt-dlp
# ydl_opts = {
#     'format': 'bestvideo+bestaudio/best',  # Download the best quality video and audio
#     'outtmpl': r'D:\videos\stories\BGRugsVideos\%(title)s.%(ext)s',  # Output file template
#     # 'noplaylist': False,  # Download all videos in the playlist
#     'playlistend': 5,  # Download only the first 5 videos in the playlist
# }
#
# # Download all videos in the playlist
# with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#     ydl.download([playlist_url])

