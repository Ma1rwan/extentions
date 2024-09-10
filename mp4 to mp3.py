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

def mp3_to_wav(mp3_file, wav_file):
    # Load the video file
    audio = AudioFileClip(mp3_file)

    # Extract the audio
    audio = audio.subclip(0.5, audio.duration)

    # Write the audio to a file
    audio.write_audiofile(wav_file)
    # Close the video and audio clips
    audio.close()


if __name__ == "__main__":
    # Example usage
    mp4_file = r"C:\Users\black2\Desktop\pygame\Carly Rae Jepsen - Call Me Maybe ｜ Piano Cover by Pianella Piano.webm"
    mp3_file = r"C:\Users\black2\Desktop\pygame/piano.wav"
    wav_file = r"C:\Users\black2\Desktop\pygame/sol-101774.wav"

    #convert_mp4_to_mp3(mp4_file, mp3_file)
    mp3_to_wav(mp4_file, mp3_file)
