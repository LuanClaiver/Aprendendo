# Aplicação de linha de comando
# Recebe um link de video de youtube
# faz download dele
from pytube import YouTube

link = input("Enter the link: ")
yt = YouTube(link)

#  Video information
print(f'Title: {yt.title}')
print(f'Number of views: {yt.views}')
print(f'Lenght of video: {yt.length}')
print(f'Description of video: {yt.description}')
print(f'Rating: {yt.rating}')

ys = yt.streams.get_highest_resolution()

print("Downloading...")
ys.download()
print("Download complete")