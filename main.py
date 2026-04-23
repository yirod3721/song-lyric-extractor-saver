from lyric_catcher import lyric_catch
from  metadata import metadata_ext
import os
song1 = 'Bruno Mars - Runaway Baby.mp3'
folder1 = input("Enter the folder containing your MP3s: ").strip()
def lyric_finder(song):
    artist_, title_, duration_1, album_ = metadata_ext(song)
    full_lyrics = lyric_catch(title_, artist_, album_, duration_1)
    if (full_lyrics == 0):
        print(f"Lyrics not found for {title_}")
    return full_lyrics

def lrc_maker(song):
    lrc_data = lyric_finder(song)
    if lrc_data == 0:
        return  1
    #extension changer
    lrc_file = os.path.splitext(song)[0] + ".lrc"
    with open(lrc_file, "w", encoding="utf-8") as f:
        try:
            f.write(lrc_data)
            print(f"Saved to {lrc_file}")
        except Exception as e:
            print(f"unable to write at {song} because {e}")
            return 1

        
    

def tester(folder):
    for filename in os.listdir(folder):
        if filename.endswith(".mp3") or filename.endswith("m4a"):
            lrc_file = os.path.splitext(filename)[0] + ".lrc"
            lrc_path = os.path.join(folder, lrc_file)
            if os.path.exists(lrc_path):
                print(f"{filename} already has an lrc file\n")
                print("skipping")
            else:
                print(f"Processing {filename}")
                lrc_maker(filename)
                print(f"filename {filename} is done")

            
            
            
    print("Done")



tester(folder1)
    



