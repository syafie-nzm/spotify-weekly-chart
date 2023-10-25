import pandas as pd

url = 'https://github.com/syafie-nzm/spotify-weekly-chart/blob/main/data/cleaned_spotify_2.csv?raw=true'
df = pd.read_csv(url)


import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=NAJWAKAMAL\SQLEXPRESS;'
                      'Database=Spotify Project;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

cursor.execute('''
		CREATE TABLE Table2 (
			Position int primary key,
			Track_URI nvarchar(250),
			Artist nvarchar(250),
			Track_Name nvarchar(250),
			Album_Name nvarchar(250),
			Artist_Popularity int,
			Artist_Genre nvarchar(250),
			Track_Popularity int,
			Danceability float,
			Energy float,
			"key" int,
			loudness float,
			mode int,
			speechiness float,
			acousticness float,
			instrumentalness float,
			liveness float,
			valence float, 
			tempo float,
			duration_ms int
			)
               ''')

for index, row in df.iterrows():
	cursor.execute('''
        INSERT INTO Table2 (Position, Track_URI, Artist, Track_Name, Album_Name, Artist_Popularity, Artist_Genre, Track_Popularity, Danceability,	Energy,	"key", loudness, mode, speechiness, acousticness, instrumentalness, liveness, valence, tempo, duration_ms)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        ''',
        row['Position'],  # Replace with the actual column names from your CSV
        row['Track URI'],
	row['Artist'], 
        row['Track Name'],
	row['Album Name'],
	row['Artist Popularity'],
	row['Artist Genre'],
	row['Track Popularity'],
	row['Danceability'],
	row['Energy'], 
	row['key'],
	row['loudness'],
	row['mode'],
	row['speechiness'],
	row['acousticness'],
	row['instrumentalness'],
	row['liveness'],
	row['valence'],
	row['tempo'],
	row['duration_ms']

    )

conn.commit()