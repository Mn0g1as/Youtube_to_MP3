from pytube import Playlist
from moviepy.editor import *

# Paste your playlist here
playlist_url = input("Paste your playlist here: ")
playlist = Playlist(playlist_url)

for video in playlist.videos:
  audio_stream = video.streams.filter(only_audio=TRUE).first()
  audio_file = audio_stream.download(output_path="mp3")
  print(f"{audio_file} finished! ")

for audio_file in os.listdir("mp3"):
  if audio_file.endswith(".mp4"):
    audio_path = os.path.join("mp3", audio_file)
    mp3_path = os.path.join("mp3" , audio_file.replace(".mp4", ".mp3"))
    audio = AudioFileClip(audio_path)
    audio.write_audiofile(mp3_path)
    os.remover(audio_path)
    print(f"{mp3_path} converted!")
