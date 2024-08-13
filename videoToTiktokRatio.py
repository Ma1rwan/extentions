import os
from moviepy.editor import VideoFileClip

# Path to the input video file
video_path = r"C:\Users\black2\Downloads\Like_click_TikTok_4k_Top3\Like_click_TikTok_4k_Top3\Like_click_TikTok_4k_GS.mp4"
# Path to the output video file
output_path = r'D:\videos\likeVideos\like1.mp4'

# Load the video file
video = VideoFileClip(video_path)
video= video.subclip(0, 7.2)
video.write_videofile(output_path, codec='libx264', audio_codec='aac')
