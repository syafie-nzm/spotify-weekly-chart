import pandas as pd

url = 'https://github.com/syafie-nzm/spotify-weekly-chart/blob/main/data/cleaned_spotify.csv?raw=true'
df = pd.read_csv(url)


import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=NAJWAKAMAL\SQLEXPRESS;'
                      'Database=Spotify Project;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

cursor.execute('''
		CREATE TABLE Top50Malaysia (
			Position int primary key,
			Artist nvarchar(250),
			Title nvarchar(250),
			Weeks int,
			Peak int,
			Streams int,
			Total int
			)
               ''')

for index, row in df.iterrows():
	cursor.execute('''
        INSERT INTO Top50Malaysia (Position, Artist, Title, Weeks, Peak, Streams, Total)
        VALUES (?,?,?,?,?,?,?)
        ''',
        row['Position'],  # Replace with the actual column names from your CSV
        row['Artist'],
        row['Title'],
	row['Weeks'],
	row['Peak'],
	row['Streams'],
	row['Total']
    )

conn.commit()