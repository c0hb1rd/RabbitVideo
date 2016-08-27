#!/usr/bin/env python
# coding=utf-8
import requests
import sys
from threading import Thread

def downloader(url, videoID):
    rep = requests.get(url)
    filename = '%d.mpeg' % videoID
    with open(filename, 'w') as f:
        f.write(rep.content)
    print('[*]Finish %d' % videoID)

url = 'http://alcdn.hls.xiaoka.tv/2016822/6a9/ccf/_TRB8bECpg3xiXtp/%d.ts'
# for i in range(1, 101):
#     Thread(target=downloader, args=(url % i, i)).start()
# downloader(url % int(sys.argv[1]), int(sys.argv[1]))
result = ''
for i in range(1, 101):
    filename = '%d.mpeg' % i
    with open(filename, 'r') as f:
        result += f.read()

with open('result.mpeg', 'w') as f:
    f.write(result)
