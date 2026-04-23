from lrclib import LrcLibAPI
import lrclib
def lyric_catch(name, artist, album, duration_):
    api = LrcLibAPI(user_agent="different-app/1.9.1")

    try:
        lyrics = api.get_lyrics(
            track_name= str(name),
            artist_name=str(artist),
            album_name=str(album),
            duration=round(duration_),
        )
        if (lyrics.synced_lyrics):
            return lyrics.synced_lyrics
        elif (lyrics.plain_lyrics):
            return lyrics.plain_lyrics
    except lrclib.exceptions.NotFoundError:
        print(f"lyrics not found for {name}")
        return 0
    except Exception as e:
        print(f"Unknown API Error has occurred with status {e} at song: {name}")
        return 0



