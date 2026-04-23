from tinytag import TinyTag

def metadata_ext(song_name):
    tag = TinyTag.get(song_name)
    return tag.artist, tag.title, tag.duration, tag.album




