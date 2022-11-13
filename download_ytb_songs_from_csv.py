from __future__ import unicode_literals
import csv
import youtube_dl

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

# place beatlist1.csv in same folder
csv_file = 'beatlist1.csv'



with open(csv_file, 'r') as f:
    lines = csv.reader(f)
    for song_num, line in enumerate(lines):
      file_name = line[1]
      ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'./downloads/{file_name}',
        'postprocessors': [{
          'key': 'FFmpegExtractAudio',
          'preferredcodec': 'mp3',
          'preferredquality': '192',
        }]
      }
      with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        if song_num == 0:
          # skip header
          continue
        print('Downloading song from {}'.format(line[0]))
        ydl.download([line[0]])

print('Finished!')