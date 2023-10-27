# Malaysia Spotify Weekly Chart

## Introduction
This repo is for documentation for simple 'data engineering' and data analysis project. Extracting spotify weekly chart (2023/10/19) for Malaysia listener. I ([Syafie](https://github.com/syafie-nzm)) as the data engineer preparing the data for further analysis, which [Najwa](https://github.com/wawalatte) the data analyst.

## Extract Transform Load (ETL) flow
![ETL](https://github.com/syafie-nzm/spotify-weekly-chart/assets/139424157/f6834bc3-9723-4cc4-a6f5-f04739f46747)


### Extract
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
There are minor cleaning and transformation made with the extracted data, some collumns in the scrapped data was not useful in my judgement, might as well get rid of it.
```python
columns_to_remove = ['Streams+', 'Change']
df = df.drop(columns=columns_to_remove)
```
Some collumns have a wrong data type which are not in our favour, it should be an integer not object. Also we cleaned the data, since it has ',' in between the number example: 10,000 (due to this the data type is object)
```python
df['Streams'] = df['Streams'].str.replace(',', '').astype(int)
df['Total'] = df['Total'].str.replace(',', '').astype(int)
```
The number data from the scrapping is not the same as from the spotify api, the spotify provides only top 50 tracks, while the kworb web serves to top 200 tracks. So we drop the rest of the tracks to make it tally.
```python
df = df.drop(index=range(50,200))
```
Finally, the data is saved in form of CSV (i dont know if this is the best practice)

### Load
I load the data into Github as middle storage system, so the data analyst can fetch the data and load it in their local RDBMS (in this case Najwa chose Microsoft SQL Server). We use pyodbc library to load the csv into MsSQLServer. \
The python codes to load the csv located in [load_data_to_MsSQL](/load_data_to_MsSQL)
