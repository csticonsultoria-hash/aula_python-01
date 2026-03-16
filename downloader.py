from pytubefix import YouTube
from pytubefix.cli import on_progress

# URL do vídeo
url = "https://www.youtube.com/watch?v=bvIMBVBRpJU"
yt = YouTube(url, on_progress_callback=on_progress)

# Selecionar a maior resolução
ys = yt.streams.get_highest_resolution()

# Baixar o vídeo
print("Baixando...")
ys.download()
print("Download concluído!")