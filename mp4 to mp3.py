from moviepy.editor import *


def convert_mp4_to_mp3(mp4_file, mp3_file):
    # Load the video file
    video = VideoFileClip(mp4_file)

    # Extract the audio
    audio = video.audio
    audio = audio.subclip(0, audio.duration)

    # Write the audio to a file
    audio.write_audiofile(mp3_file)
    # Close the video and audio clips
    video.close()
    audio.close()

def mp3_to_wav(mp3_file, wav_file):
    # Load the video file
    audio = AudioFileClip(mp3_file)

    # Extract the audio
    audio = audio.subclip(6, audio.duration)

    # Write the audio to a file
    audio.write_audiofile(wav_file)
    # Close the video and audio clips
    audio.close()


if __name__ == "__main__":
    # Example usage
    mp4_file = r"C:\Users\black2\Videos\MEmu Video\charli xcx - 365 [ sped up ] lyrics.webm"
    mp3_file = r"C:\Users\black2\Videos\MEmu Video\charli xcx - 365 [ sped up ] lyrics.mp3"
    #wav_file = r"C:\Users\black2\Desktop\pygame/doki.wav"

    convert_mp4_to_mp3(mp4_file, mp3_file)
    #convert_mp4_to_mp3(mp4_file, wav_file)
