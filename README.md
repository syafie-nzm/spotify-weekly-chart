# Malaysia Spotify Weekly Chart

## Introduction
This repo is for documentation for simple 'data engineering' project. Extracting spotify weekly chart (2023/10/19) for Malaysia listener.

## Export Transform Load (ETL) flow
![ETL](https://github.com/syafie-nzm/spotify-weekly-chart/assets/139424157/f6834bc3-9723-4cc4-a6f5-f04739f46747)


### Export
There are two sources we extract data from:
- [Spotify API](https://developer.spotify.com/documentation/web-api)
- [Kworb.net](https://kworb.net/spotify/country/my_weekly.html)

#### Spotify API
With Spotify API we can extract tracks information from the [Top Songs - Malaysia](https://open.spotify.com/playlist/37i9dQZEVXbKcS4rq3mEhp?si=df6c4becdaab41f4) such as Track Title, Artist Name, Track and Artist Popularity, Track and Artist URI (useful for extracting Artist's genre, and tracks audio features). For the audio features of every tracks we can get the information on the track's danceability, loudness, speechness, acousticness, track duration etc.
#### Kworb.net
Since spotify api does not provide data on stream number of every track, I found other source that provide that information. It also provide the data on Malaysian listener. The cons of this source is that, the total streams data was not the total streams of the song since the begining of time, yet it was total streams when the song is IN the Top Weekly Chart playlist. However it has the weekly streams of the song (how many it was played within the week).\
\
This source was extracted by scrapping the website using BeautifulSoup.

### Transform
