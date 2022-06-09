Title: How to Fetch YouTube subs using Python and youtube-transcript-api (pip pkg)
Date: 2022-06-09
Category: Web tricks using Python
Tags: python, web, YouTube, Transcription, video, subtitles
Author: Daniel Muyshond
Summary: It is a small test of that python package that allows to fetch YouTube subtitles, even if they are automated, which is pretty cool.

## Fetching subtitles (even the automated ones!)

Here is the code snippet I just made trying out that amazing package :

```
from youtube_transcript_api import YouTubeTranscriptApi

video_id = input('What is the id of the video (after "watch?v=")? : ')
transcription = YouTubeTranscriptApi.get_transcript(video_id)
#  print(transcription)

for el in list:
    print(el["text"])

"""
You can also add the languages param
if you want to make sure the transcripts
are retrieved in your desired language
(it defaults to english).
"""
# YouTubeTranscriptApi.get_transcripts(video_ids, languages=['de', 'en'])
```

https://pypi.org/project/youtube-transcript-api/
