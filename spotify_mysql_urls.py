import re
import mysql.connector
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy

# Set up Spotify API credentials
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id='client-id',  # Replace with your Client ID
    client_secret='secret-id'  # Replace with your Client Secret
))

# MySQL server connection (without specifying database yet)
server_connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root'
)
server_cursor = server_connection.cursor()

# Create database if it doesn't exist
server_cursor.execute("CREATE DATABASE IF NOT EXISTS spotify_db")
server_cursor.close()
server_connection.close()

# Connect to the specific database now
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'spotify_db'
}
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

# Create table if it doesn't exist
create_table_query = """
CREATE TABLE IF NOT EXISTS spotify_tracks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    track_name VARCHAR(255),
    artist VARCHAR(255),
    album VARCHAR(255),
    popularity INT,
    duration_minutes FLOAT
)
"""
cursor.execute(create_table_query)

# ✅ Absolute path to your track_urls.txt file
file_path = r"C:\Users\sanji\Downloads\spotify_data_analytics-main\spotify_data_analytics-main\track_urls.txt"

# Read track URLs from file
with open(file_path, 'r') as file:
    track_urls = file.readlines()

# Process each URL
for track_url in track_urls:
    track_url = track_url.strip()
    try:
        # Extract track ID from URL
        track_id = re.search(r'track/([a-zA-Z0-9]+)', track_url).group(1)

        # Fetch track details from Spotify API
        track = sp.track(track_id)

        # Extract metadata
        track_data = {
            'Track Name': track['name'],
            'Artist': track['artists'][0]['name'],
            'Album': track['album']['name'],
            'Popularity': track['popularity'],
            'Duration (minutes)': track['duration_ms'] / 60000
        }

        # Insert data into MySQL
        insert_query = """
        INSERT INTO spotify_tracks (track_name, artist, album, popularity, duration_minutes)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (
            track_data['Track Name'],
            track_data['Artist'],
            track_data['Album'],
            track_data['Popularity'],
            track_data['Duration (minutes)']
        ))
        connection.commit()

        print(f"Inserted: {track_data['Track Name']} by {track_data['Artist']}")

    except Exception as e:
        print(f"Error processing URL: {track_url}, Error: {e}")

cursor.close()
connection.close()

print("All tracks have been processed and inserted into the database.")
