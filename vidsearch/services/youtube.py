from pytubefix import YouTube


def download_audio(url: str) -> None:
  return YouTube(url).streams\
    .filter(only_audio=True)\
    .first()\
    .download()