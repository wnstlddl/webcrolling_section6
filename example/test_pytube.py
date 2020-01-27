import pytube
import sys
import io
import os
import subprocess

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding = 'utf-8')
#다운받을 URL 지정

url = 'https://www.youtube.com/watch?v=p55FXmfbTPg'

yt = pytube.YouTube(url)
videos = yt.streams.all()

for i in range(len(videos)):
    print(i,' : ',videos[i])
