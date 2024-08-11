from moviepy.editor import *


def convert_mp4_to_mp3(mp4_file, mp3_file):
    # Load the video file
    video = VideoFileClip(mp4_file)

    # Extract the audio
    audio = video.audio
    audio = audio.subclip(16, audio.duration)

    # Write the audio to a file
    audio.write_audiofile(mp3_file)
    # Close the video and audio clips
    video.close()
    audio.close()


if __name__ == "__main__":
    # Example usage
    mp4_file = r"C:\Users\black\Downloads\Video/gvif.mp4"
    mp3_file = r"C:\Users\black\Downloads\Video/audio.mp3"
    convert_mp4_to_mp3(mp4_file, mp3_file)
