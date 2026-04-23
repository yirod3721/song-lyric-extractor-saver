# song-lyric-extractor-saver

🎵 Lyrics Fetcher (.lrc Generator)

A Python script that scans your music folder, fetches lyrics using LRCLIB, and saves them as .lrc files next to your songs.

Supports MP3 and M4A files, with metadata extracted via TinyTag.


---

✨ Features

Works with .mp3 and .m4a files

Prompts you for a folder at runtime (no arguments needed)

Automatically extracts artist and title

Fetches synced lyrics when available

Saves .lrc files with matching filenames

Skips files that already have lyrics

Graceful error handling (missing metadata, no lyrics found, etc.)



---

📦 Requirements

Python 3.8+

Libraries:

tinytag

lrclib



Install dependencies:

pip install tinytag lrclib


---

▶️ Usage

Run the script:

python3 main.py

You’ll be prompted to enter the path to your music folder:

Enter music folder path: /path/to/your/music

The script will then:

1. Scan the folder for audio files


2. Fetch lyrics using LRCLIB


3. Save them as .lrc files




---

📁 Example

Input:

song - name.mp3

Output:

song - name.lrc


---

⚠️ Notes

Lyrics availability depends on the LRCLIB database

Some songs may not have lyrics available

Correct metadata (artist/title) improves results

Not all lyrics are time-synced



---

🛠️ Future Improvements

Recursive folder scanning

Progress indicator

Better metadata cleanup

Fallback lyrics sources

GUI version



---
