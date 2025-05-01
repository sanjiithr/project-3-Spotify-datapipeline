Here’s a **GitHub README.md** based on our entire chat — covering your Spotify Data Pipeline project from API access to MySQL integration, data analysis, and visualization:

---

# 🎧 Spotify Data Pipeline Project

This project is a complete **ETL pipeline** built with Python that extracts data from the Spotify Web API, transforms it, and loads it into a **MySQL database**. It also supports **basic analytics and visualization** using pandas and matplotlib.

---

## 📌 Features

- ✅ Extracts track metadata using the Spotify Web API  
- ✅ Processes batch track URLs from a text file  
- ✅ Loads track data into a MySQL database  
- ✅ Visualizes track popularity and duration  
- ✅ Saves data into a CSV file  
- ✅ Modular and customizable

---

## 📂 Project Structure

```
spotify_data_pipeline/
├── spotify_mysql_urls.py       # Main ETL script
├── track_urls.txt              # Input file containing Spotify track URLs
├── spotify_track_data.csv      # Exported track data (after ETL)
├── README.md                   # This file
```

---

## 🚀 How to Run

### 1. **Clone the repo**
```bash
git clone https://github.com/yourusername/spotify-data-pipeline.git
cd spotify-data-pipeline
```

### 2. **Install dependencies**
Ensure you're in a virtual environment or Anaconda, then install:
```bash
pip install spotipy mysql-connector-python pandas matplotlib
```

### 3. **Set up MySQL**

1. Start your MySQL server (e.g., using XAMPP or MySQL Workbench)
2. Create a database:
```sql
CREATE DATABASE spotify_db;
```

3. Create the table:
```sql
USE spotify_db;

CREATE TABLE spotify_tracks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    track_name VARCHAR(255),
    artist VARCHAR(255),
    album VARCHAR(255),
    popularity INT,
    duration_minutes FLOAT
);
```

### 4. **Set up your Spotify Developer credentials**
- Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
- Create an app and get your:
  - `Client ID`
  - `Client Secret`

Update them in your Python script.

---

## 📝 Usage

### **Batch Mode: Run ETL on a List of Tracks**

Update `track_urls.txt` with links like:

```
https://open.spotify.com/track/361FMJC5uRSXzato4NE5Zg
https://open.spotify.com/track/7qiZfU4dY1lWllzX7mPBI3
...
```

Then run:

```bash
python spotify_mysql_urls.py
```

Track data will be fetched, saved to MySQL, and written to CSV.

---

### **Single Track Visualization (Optional)**

Use this snippet for quick visualization of a single track:

```python
# Replace with your track URL
track_url = "https://open.spotify.com/track/361FMJC5uRSXzato4NE5Zg"
```

The script will show:

- Track metadata
- Bar chart of popularity and duration
- Data saved to `spotify_track_data.csv`

---

## 📊 Example Output

```
Track Name: Hukum
Artist: Anirudh Ravichander
Album: Jailer (Original Soundtrack)
Popularity: 78
Duration: 4.13 minutes
```

📈 *Bar chart will show after script execution.*

---

## 🔐 Troubleshooting

- `Unknown database 'spotify_db'`: Create the database manually in MySQL first.
- `'mysql' is not recognized`: Ensure MySQL is added to your system PATH or use MySQL Workbench/XAMPP.
- `FileNotFoundError: track_urls.txt`: Use absolute path or ensure the file exists.
- `Spotify API authentication error`: Make sure you’ve set the correct client ID and secret.

---

## 🙌 Credits

Built with:
- [Spotipy](https://spotipy.readthedocs.io/)
- [MySQL Connector](https://pypi.org/project/mysql-connector-python/)
- [Matplotlib](https://matplotlib.org/)
- [Pandas](https://pandas.pydata.org/)

---

