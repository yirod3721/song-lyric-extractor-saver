from lyric_catcher import lyric_catch
from  metadata import metadata_ext
import os
def lyric_finder(song):
    artist_, title_, duration_1, album_ = metadata_ext(song)
    print(f"the artist is {artist_} and the title is {title_} and the duration is {duration_1} and it belongs to {album_}")
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
                mp3_path = os.path.join(folder, filename)
                print(f"Processing {mp3_path}")
                lrc_maker(mp3_path)
                print(f"filename {filename} is done")

            
            
            
    print("Done")
def individual_song(song):
    song_path = os.path.join('.', song)
    for filename in os.listdir('.'):
        if os.path.exists(song_path):
            print("MP3 file found, currently processing...")
            lrc_maker(song_path)
            print(f"{song} has been processed")
            return 0
        else:
            print(f"file under name {song} in {song_path} not found")
            return 1


def main():
    choice = str(input("enter song for individual song lyrics and folder for folder scan lyric function: "))
    while (choice != "song") and (choice != "folder"):
        print("Please enter either song or folder")
        choice = str(input("enter song for individual song lyrics and folder for folder scan lyric function: "))
    if (choice == "song"):
        song1 = str(input("Enter the mp3 file name: "))
        individual_song(song1)
    if (choice == "folder"):
        folder1 = input("Enter the folder containing your MP3s: ").strip()
        tester(folder1)
    print("Thank you for using my program")




main()





        
    

    



